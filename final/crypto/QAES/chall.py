#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Util.Padding import pad
from os import urandom
import binascii
import random

with open("flag.txt", "rb") as f:
    FLAG = f.read()

keyA = urandom(16)
keyB = b"v3rys3cur3pwd!"
keyC = urandom(16)
keyD = keyB + keyA[len(keyB):]
keyE = urandom(16)
noise = urandom(random.randint(1, 3))

def encrypt(plain: bytes, with_key: bool):
    if with_key:
        plain = pad(plain + noise + keyE, 16)
    else:
        plain = pad(plain, 16)

    aes0 = AES.new(keyD, AES.MODE_CBC, iv=keyE)
    aes1 = AES.new(keyA, AES.MODE_CTR, counter=Counter.new(128))
    aes2 = AES.new(keyC, AES.MODE_OFB, iv=keyE)
    aes3 = AES.new(keyE, AES.MODE_ECB)

    res0 = aes0.encrypt(plain)
    res1 = aes1.encrypt(res0)
    res2 = aes2.encrypt(res1)
    res3 = aes3.encrypt(res2)
    print("Result:", res3.hex())

if __name__ == "__main__":
    while True:
        print("[1] Get Encrypted flag")
        print("[2] Encrypt text")
        print("[3] Exit")
        inp = input("Input: ")

        if inp == "1":
            encrypt(FLAG, False)
        elif inp == "2":
            plain = input("Plain (hex): ")
            encrypt(binascii.unhexlify(plain), True)
        elif inp == "3":
            print("Cya!!")
            exit()
        else:
            print("???")
        print()
