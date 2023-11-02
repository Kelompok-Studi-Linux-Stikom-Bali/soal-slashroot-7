#!/usr/bin/env python3

import ecdsa
import random
import hashlib

from Crypto.Util.number import *
from secret import flag

num = getPrime(512)

u = random.randint(1, num-5)
v = random.randint(1, num-5)

assert u < num
assert v < num 

def gen_k(num, w):
    return num, (u * w + v) % num

k = gen_k(num, 655357)
user_k = gen_k(num, k[1])

def sign(k, m):
    G = ecdsa.NIST256p.generator
    n = G.order()
    nonce = random.randrange(1,n)

    pub_key = ecdsa.ecdsa.Public_key(G, G * nonce)
    priv_key = ecdsa.ecdsa.Private_key(pub_key, nonce)

    m = int(hashlib.sha256(m.encode()).hexdigest(),base=16)
    sig = priv_key.sign(m, k)

    return sig, nonce, m

def sign_flag(k):
    enc = sign(k, flag)

    return enc

def banner():
    msg = '''
     $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$$$\ 
    $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  _____|
    $$ /  $$ |$$ /  \__|$$ |  $$ |$$ /  \__|$$ |      
    $$$$$$$$ |\$$$$$$\  $$ |  $$ |$$ |      $$$$$\    
    $$  __$$ | \____$$\ $$ |  $$ |$$ |      $$  __|   
    $$ |  $$ |$$\   $$ |$$ |  $$ |$$ |  $$\ $$ |      
    $$ |  $$ |\$$$$$$  |$$$$$$$  |\$$$$$$  |$$$$$$$$\ 
    \__|  \__| \______/ \_______/  \______/ \________|
    '''
    print(msg)

def main():
    banner()
    
    flag_sig = sign_flag(k[0])

    print(f'''
    Welcome to my signature maker
    before we proceed i wanna give you something

    here it is :
    secret msg        : {flag_sig[2]}
    (r,s)             : ({flag_sig[0].r}, {flag_sig[0].s})
    u                 : {u}
    v                 : {v}    
    (p * r + q) % num : {k[1]}

    to ensure that you worth this gift go find it's nonce and give it to me
    ''')

    while True:
        print('''
    enjoy my service

    1) read gift
    2) create new signature
    3) exit
        ''')

        choise = int(input("    what you gonna do : "))

        if choise == 1:
            priv_key = flag_sig[1]
            verify = int(input("\n    Give me your nonce : "))
            if verify == priv_key:
                print(f"    Here is your gift : {flag}")
            else:
                print("Try again")
                exit()
        elif choise == 2:
            msg = input('\n    your msg : ')
            user_sig = sign(user_k[0], msg)
            print(f'    your signature    : ({user_sig[0].r},{user_sig[0].s})')
            print(f'    (p * r + q) % num : {user_k[1]}')
        elif choise == 3:
            exit()
        else:
            print("Not a valid option!")
            exit()

if __name__ == '__main__':
    main()