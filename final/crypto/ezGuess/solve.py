from Crypto.Util.number import inverse
from crackLCG import crack_LCG
from pwn import *

p = remote("165.232.168.88", 1121)

dummy_char = b"A"*16
p.sendline(dummy_char)
p.recvuntil(b"Here you go: ")
result = eval(p.recvline().strip())
states = [a^b for a,b in zip(result[-16:], dummy_char)]

n,m,c = crack_LCG(states)
prev_states = [states[0]]

for i in range(len(result[:-16])):
    x = (inverse(m,n)*(prev_states[i]-c)) % n
    prev_states.append(x)

prev_states = prev_states[::-1]

flag = ''.join([chr(a^b) for a,b in zip(result[:-16], prev_states)])[:-2]
print(f"slashroot7{{{flag}}}")
