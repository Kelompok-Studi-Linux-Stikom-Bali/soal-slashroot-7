from pwn import *
from Crypto.Util.number import *
# context.log_level = "debug"

p = process('./chall.py')
p.recvuntil(b"n : ")
n = int(p.recvline().strip())
p.recvuntil(b"\n")
e = 65537
p.recvuntil(b":")
p.sendline(b"-65537")
d = int(p.recvuntil(b"\n").strip())
p.recvline()
p.recvuntil(b"can you decrypt this?")
p.recvline()
c = int(p.recvline().strip())
p.recvline()
m = pow(c, -d, n)
p.recvuntil(b':')
p.sendline(str(m).encode())
p.interactive()