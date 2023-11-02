#!/usr/bin/env python3
import secret

class random:
    def __init__(self, seed):
        self.mod = secret.N
        self.mult = secret.M
        self.inc = secret.I
        self.state = seed

    def generate(self):
        self.state = (self.state * self.mult + self.inc) % self.mod
        return self.state

flag_content = secret.FLAG
seed = secret.STATE
r = random(seed)

if __name__ == "__main__":
    msg = input("Your message: ")
    plain = flag_content + "||" + msg
    res = [r.generate() ^ ord(x) for x in plain]
    print(f"Here you go: {res}")
    exit()