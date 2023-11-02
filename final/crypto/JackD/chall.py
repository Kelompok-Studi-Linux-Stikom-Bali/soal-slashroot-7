from sage.all import *
from Crypto.Util.number import bytes_to_long as b2l, long_to_bytes as l2b, getPrime as gp
from binascii import hexlify
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

flag = open('flag.txt','rb').read()

p = gp(512)  
q = gp(512)
n = p * q
phi = (p - 1) * (q - 1)

e = 65537  
d = inverse_mod(e, phi) 

dp = d % (p - 1)
dq = d % (q - 1)
qinv = inverse_mod(q, p)

message = b2l(flag)

ciphertext = l2b(power_mod(message, e, n))


private_key = rsa.RSAPrivateNumbers(
    p,
    q,
    int(d),
    int(dp),
    int(dq),
    int(qinv),
    rsa.RSAPublicNumbers(e, n)
).private_key(default_backend())

print(dp, dq, qinv)

with open('flag.enc','wb') as f:
    f.write(
        hexlify(ciphertext)
    )

with open("private_key.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ))