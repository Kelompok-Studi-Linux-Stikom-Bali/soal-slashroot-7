from pwn import *

coll = 'echo 0004812028 | cat *'

p = process('./chall.py')
p.sendline(coll)
p.interactive()