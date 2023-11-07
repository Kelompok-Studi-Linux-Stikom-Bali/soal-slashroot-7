from Crypto.Util.number import *
from functools import reduce

class LCG:
    def __init__(self, state, modulus, multiplier, increment):
        self.state = state
        self.modulus = modulus
        self.multiplier = multiplier
        self.increment = increment
    
    def next(self):
        self.state = (self.state * self.multiplier + self.increment) % self.modulus
        return self.state

def crack_LCG(states, modulus=0, multiplier=0, increment=0):
    # crack modulus
    if modulus == 0:
        t = []
        for i in range(len(states) - 1):
            t.append(states[i+1] - states[i])
        u = []
        for i in range(len(t) - 2):
            result = abs(t[i+2] * t[i] - t[i+1]**2)
            u.append(result)
        modulus = reduce(GCD, u)

    # crack multiplier
    if multiplier == 0:
        multiplier = (states[2] - states[1]) * inverse(states[1] - states[0], modulus) % modulus

    # crack increment
    if increment == 0:
        increment = (states[1] - states[0]*multiplier) % modulus

    return modulus, multiplier, increment