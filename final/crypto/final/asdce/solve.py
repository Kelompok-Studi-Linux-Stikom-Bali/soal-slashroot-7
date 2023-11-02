import ecdsa
import ast
import libnum
from pwn import *
from Crypto.Util.number import *


def get_z2():
    p.sendline(b'2')
    p.sendline(b'hello')
    p.recvuntil(b'(p * r + q) % num : ')
    z2 = int(p.recvline().strip().decode())
    return z2

def compute_k(u,v,w,z1,z2):
    f1 = z1 - (u * w + v)
    f2 = z2 - (u * (u * w + v) + v)
    k = GCD(f1,f2)
    return k

# def compute_priv_key()

p = process('./chall.py')
p.recvuntil(b'here it is :')
p.recvline()
p.recvline()
p.recvuntil(b'(r,s)             : ')

sig = ast.literal_eval(p.recvline().strip().decode())
r,s = sig[0], sig[1]

p.recvuntil(b'u                 : ')
u = int(p.recvline().strip().decode())

p.recvuntil(b'v                 : ')
v = int(p.recvline().strip().decode())

w = 655357

p.recvuntil(b'(p * r + q) % num : ')
z1 = int(p.recvline().strip().decode())
z2 = get_z2()

k = compute_k(u,v,w,z1,z2)

G = ecdsa.NIST256p.generator
n = G.order()

r_inv = libnum.invmod(r, n)
m = 99361453254494854334746693466951066897436662658100419567395144469174038347298
try_private_key = (r_inv * ((k * s) - m)) % n

p.sendline(b'1')
p.sendline(str(try_private_key).encode('latin1'))

info(f'r\t   : {r}')
info(f's\t   : {s}')
info(f'u\t   : {u}')
info(f'v\t   : {v}')
info(f'w\t   : {w}')
info(f'z1\t  : {z1}')
info(f'z2\t  : {z2}')
info(f'k\t   : {k}')
info(f'n\t   : {n}')
info(f'priv\t: {try_private_key}')

p.interactive()