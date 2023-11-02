from base64 import b64decode
from binascii import unhexlify
from Crypto.Util.number import *

# key64 = b'MIICXAIBAAKBgQCfUcF4kbLiTD35FFssnJCMV/g7EqTO8CkUMWHTOJ5xcSebzGSNu/HzaYUC+dLM/SG5wQuo1O00ZtfyTyqgx2oMDr1/U1A70xycddVd+PNiUasTYZyVGV3uA1E7DGyWXqkmfG/v/atZA08v2tkRY+iP7eKYSO7GRsDUjFk8L5e7VQIDAQABAoGBAJ1hIpAaxS2ciP+a5zHbe0LXx4N7OEifnsSuv2bqoEGJuMnDj3UfOrPsAZPd+ym5x+35z624oJVKHnnjUEXAl3TAT9vlvj17uryb7fXRiGdKQ1HK2GnPpEbSdn83sR4xipk8AlOx+au+FZ7dn0tMeSYYA8alBOfOefhLQypvlMfBAkEA055rARIKaAIJH9xP+VRAcd17ZweC7fbUmfvd8BHj5Ln8D4MlMJduiCsa4K61Kw+L8MF/hSdVgYyd0t72FVVeUQJBAMC7b+W+Q+q5rVM36O++eqR/WVNcQaIdmR4uEhmi5mDcT/QnPAtVXom0DkIA2hLkZt7P1yGmIkBe49Ehc+EG98UCQFbss7d02aFvdKAJtzALU41yFMZ1Z2qoARxfQQLj1mCVpNwaWqRjD5wPWLMCEJjngewbD256gbz9Lbb4rsyEjIECQEU0CF3KD8D8osu6y50qHAds4roX6kk3r38ys7UY1Pf6o4rbe6fmI2f2ixgQDj2yXW2r22dtq+bJK6wwAtfOFLECQE2+WGuP9ZZlv41cHCbgTLC0NZDwPJc9+4TIJcEwcHsl+MUvmvxrpBqvdqFXPkgpEr2idLOenEn+0ehyIITOuE4='

key64 = 'QGkbG7Wg3063tfJddgp+oarLP7eNgdonZwJAQTCuJcml5NVSXGHNm5zGEgurAljriKwntGOepZS6Jgm9S9N4xwJ7UadtxPhKvp9jkQA7wWimNfUnNaJf0/X5EQJAVfGbuFQEOwqiItYMJRPIcXJ9M8KpLzxrBd3lrEl149kQ8lFk7FvFv5d/g0seN6vJ5wo7Sqco7LFUjQ35k+kZUwJBAJM2ZkwzYWxoLWs7b5JdYk4sAYd3rV/54Byatl05qUSWtBx3ZNapjYVQossEXMhCapOnWq9bvengRGn2kAXkIQI='

def get_dp_dq_qinv(key64):
    result = []
    key_tab = list(b64decode(key64))
    i = 0
    while i < len(key_tab):
        x = key_tab[i]
        if x == 0x2:  # integer start
            length = key_tab[i + 1]
            octets = key_tab[i + 2: i + 2 + length]
            value = int.from_bytes(octets, byteorder="big")
            result.append(value)
            i += 2 + length
        else:
            i += 1
    return tuple(result)

def recover_parameters(dp, dq, qinv, e):
    results = []
    d1p = dp * e - 1
    for k in range(3, e):
        if d1p % k == 0:
            hp = d1p // k
            p = hp + 1
            if isPrime(p):
                d1q = dq * e - 1
                for m in range(3, e):
                    if d1q % m == 0:
                        hq = d1q // m
                        q = hq + 1
                        if isPrime(q):
                            if (qinv * q) % p == 1 or (qinv * p) % q == 1:
                                results.append((p, q, e))
                                return p,q,e
    return results

def egcd(a, b):
    u, u1 = 1, 0
    v, v1 = 0, 1
    while b:
        q = a // b
        u, u1 = u1, u - q * u1
        v, v1 = v1, v - q * v1
        a, b = b, a - q * b
    return u


def get_d(p, n, e):
    q = n / p
    phi = (p - 1) * (q - 1)
    d = egcd(e, phi)
    if d < 0:
        d += phi
    return d

dp, dq, qinv = get_dp_dq_qinv(key64)
e = 65537
p, q, e = recover_parameters(dp, dq, qinv, e)
n = p * q

d = inverse(e,(p - 1) * (q - 1))

ct = open('flag.enc','rb').read()
ct = unhexlify(ct)
ct = bytes_to_long(ct)

flag = long_to_bytes(pow(ct,d,n))

print(f"p : {p}")
print(f"q : {q}")
print(f"n : {n}")
print(f"e : {e}")
print(f"d : {d}")

print(f"\nFlag : {flag.decode()}")