from Crypto.Util.number import *
from secret import flag
from binascii import hexlify
import sympy


p = getPrime(512)
q = getPrime(512)
n = p*q
e = 65537

s = pow(2,p,n)

m = bytes_to_long(flag)
c = pow(m, e, n)

with open('output.txt','w') as f:
    f.write(f"n : {str(n)}\ne : {str(e)}\nc : {str(c)}\ns : {str(s)}")