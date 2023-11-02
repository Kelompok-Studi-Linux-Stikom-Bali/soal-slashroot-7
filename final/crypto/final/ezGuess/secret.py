from Crypto.Util.number import getPrime, GCD
import random

def generate_state():
    n = getPrime(30)
    phi = n-1
    m = random.randint(1<<29, n)
    while GCD(m, phi) != 1 and n < m:
        m = random.randint(1<<29, n)
    
    i, state = random.randint(1<<29, n), random.randint(1<<29, n)
    while i > n:
        i = random.randint(1<<29, n)

    while state > n:
        state = random.randint(1<<29, n)

    return n, m, i, state

FLAG = "pretty_ez_guessing_game_i_guess"
N, M, I, STATE = generate_state()