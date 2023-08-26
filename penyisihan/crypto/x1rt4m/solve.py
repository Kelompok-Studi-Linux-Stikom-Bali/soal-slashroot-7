from binascii import unhexlify
# from secret import flag

# import string
# import random
import numpy as np

def xor(a, b):
    return [ord(x)^y for x,y in zip(a,b)]

def pad(text):
    padding_len = 16 - (len(text) % 16)
    return text + bytes([padding_len]) * padding_len

def t2m(s,r,c):
    if len(s) != (r * c):
        print("Incorect Matrix Size!")
        exit()

    ascii_values = np.zeros(len(s), dtype=int)

    for i, char in enumerate(s):
        ascii_values[i] = ord(char)

    matrix = np.reshape(ascii_values, (r, c))

    return matrix

def decrypt(ciphertext, key, iv):

    ct_block = [ciphertext[i:i+16] for i in range(0,len(ciphertext),16)]
    init = iv

    pt = []

    for block in ct_block:
        plaintext_block = init
        result = xor(plaintext_block, block)
        pt.append(result)
        init = plaintext_block

    x = [j for i in pt for j in i]
    a = np.array([x[i:i+2] for i in range(0,len(x),2)])

    flag_list = [round(j) for i in np.dot(a, np.linalg.inv(key)).T.tolist() for j in i]

    flag = ''

    for i in flag_list:
        flag += chr(i)

    return unhexlify(flag)

key = 'CRXD'
IV = list(pad(b'slashroot7{').decode()) # are u lucky enough to guess the IV? well, i doubt it hahahaha
key2matrix = t2m(key,2,len(key)//2)
ct = [8510, 8278, 8336, 7945, 8130, 7850, 10758, 11289, 8574, 8159, 8048, 7619, 8520, 8255, 7820, 7579, 8233, 7948, 12761, 11643, 8349, 8068, 12361, 11123, 8574, 8159, 11745, 12109, 8375, 8097, 15727, 15237, 8430, 8158, 12493, 11187, 8065, 7900, 8066, 8005, 8505, 8205, 10925, 11433, 8520, 8255, 8237, 7809, 8569, 8068, 10760, 11269, 8485, 8264, 8022, 7753, 7955, 7857, 11081, 11625, 8023, 7825, 7793, 7593, 7930, 7666, 7433, 7191, 8546, 8090, 15520, 14981, 7825, 7785, 8279, 7941, 7770, 7615, 11591, 12033, 7830, 7730, 8135, 7727, 7821, 7724, 8192, 7997, 7894, 7739, 11396, 11959, 7770, 7615, 11591, 12033]

print(f"flag : {decrypt(ct,key2matrix,IV).decode()}")