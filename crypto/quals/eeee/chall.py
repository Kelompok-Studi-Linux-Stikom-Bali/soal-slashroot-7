#! /usr/bin/python3

from Crypto.Util.number import *
from secret import flag

e = 65537

while True:
    p,q = getPrime(1024), getPrime(1024)
    n = p * q
    phi = (p - 1) * (q - 1)
    if GCD(e,phi) == 1:
        break

print(f'n : {n}')
print(f'e : {e}')

while True:
    e_user = int(input('\nyour e : '))
    if e_user == e or e_user == -1:
        print('\nbruh, dont cheat!')
        break

    try:
        print(inverse(e_user,phi))
    except:
        print('\nyour number is uninvertable!')
        continue

    m = getPrime(1024)
    c = pow(m,e,n)

    print("\ncan you decrypt this?")
    print(c)
    
    user_ans = int(input('\nyour guess : '))
    
    if user_ans == m:
        print(m)
        print(user_ans)
        print(flag)
        break
    else:
        print('\nbyebye!')