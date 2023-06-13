#!/usr/bin/python3

# from Crypto.Util.number import *
# from Crypto.Random.random import getrandbits, randint
# from math import gcd
# from se

# e = 65537

# while True:
#     p = getPrime(1024)
#     q = getPrime(1024)
#     n = p * q
#     phi = (p - 1) * (q - 1)
#     if gcd(e, phi) == 1:
#         break

# print(f"n = {n}")
# print(f"e = {e}")

# while True:
#     chosen_e = int(input("Give me an `e`, and I'll give you a `d`: "))
#     if chosen_e == e:
#         print("Nice try!")
#         break
#     try:
#         print(pow(chosen_e, -1, phi))
#     except:
#         print("That's not invertible :pensive:")
#         continue
#     m = getrandbits(1024)
#     c = pow(m, e, n)
#     print("If you can decrypt this, I'll give you a flag!")
#     print(c)
#     ans = int(input("Your answer: "))
#     if ans == m:
#         print(flag)
#         break
#     else:
#         print("Numbers, am I right :pensive:")


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
    if e_user == e:
        print('\nbruh, dont cheat!')
        break

    try:
        print(pow(e_user,-1,phi))
    except:
        print('\nyour number is uninvertable!')
        continue

    m = getPrime(1024)
    c = pow(m,e,n)

    print("\ncan you decrypt this?")
    print(c)
    
    user_ans = int(input('\nyour guess : '))

    if user_ans == m:
        print(flag)
        break
    else:
        print('\nbyebye!')