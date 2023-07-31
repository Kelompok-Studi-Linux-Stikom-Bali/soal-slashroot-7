import random
from Crypto.Util.Padding import pad

N_ROUNDS = 10

def bytes2matrix(text):
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    return bytes(sum(matrix, []))


def gen_sbox():
    sbox = list(range(256))
    random.shuffle(sbox)
    return sbox

sbox = gen_sbox()

def shift_rows(s):
    s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]
    return s

xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)

def mix_single_column(a):
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)

def mix_columns(s):
    for i in range(4):
        mix_single_column(s[i])
    return s

def add_round_key(s, k):
    return [[sss^kkk for sss, kkk in zip(ss, kk)] for ss, kk in zip(s, k)]


def expand_key(master_key):
    r_con = (
        0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
        0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
        0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
        0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
    )

    key_columns = bytes2matrix(master_key)
    iteration_size = len(master_key) // 4

    i = 1
    while len(key_columns) < (N_ROUNDS + 1) * 4:
        word = list(key_columns[-1])

        if len(key_columns) % iteration_size == 0:
            word.append(word.pop(0))
            word = [sbox[b] for b in word]
            word[0] ^= r_con[i]
            i += 1
        elif len(master_key) == 32 and len(key_columns) % iteration_size == 4:
            word = [sbox[b] for b in word]

        word = bytes(i^j for i, j in zip(word, key_columns[-iteration_size]))
        key_columns.append(word)

    return [key_columns[4*i : 4*(i+1)] for i in range(len(key_columns) // 4)]

def xor_bytes(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

def sub_bytes(s, sbox=sbox):
    return [[sbox[i] for i in j] for j in s]
    

def encrypt_block(block, key):
    state = add_round_key(block, key[0])
    
    for i in range(1, 10):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, key[i])

    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, key[-1])

    return state

def encrypt(data, key):
    key_schedule = expand_key(key)

    padding_len = 16 - (len(data) % 16)
    data += bytes([padding_len] * padding_len)
    
    blocks = bytes2matrix(data)

    return matrix2bytes(encrypt_block(blocks,key_schedule))

plaintext = b'indraganteng123'
key = bytes.fromhex('2b7e151628aed2a6abf7158809cf4f3c')
ciphertexts = encrypt(plaintext, key)

print(recovered_key)