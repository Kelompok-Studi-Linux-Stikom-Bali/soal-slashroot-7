from binascii import hexlify, unhexlify
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from itertools import permutations
from pwn import remote, xor

class Remote:
    def __init__(self, ip, port) -> None:
        self.p = remote(ip, port)

    def send(self, choice: bytes, data: bytes | None = None):
        self.p.sendline(choice)
        if data != None:
            self.p.sendline(data)

        self.p.recvuntil(b"Result: ")
        res = self.p.recvline().strip()

        return res

    def close(self):
        self.p.close()

p = Remote("165.232.168.88", 1131)

try:
    enc_flag = p.send(b"1")

    # guess noise length
    l = 0
    noise_len = 0
    for i in range(1, 16):
        dummy = hexlify(b"A" * i)
        res = p.send(b"2", dummy)
        if l == 0:
            l = len(res)
        elif len(res) != l:
            noise_len = 16 - i
            break
    print("noise length ->", noise_len)

    # padding attack
    keyE = b""
    for i in range(16 + noise_len):
        dummy = hexlify(b"A" * (31 - i))
        sample = p.send(b"2", dummy)
        sample_block = [sample[i:i+32] for i in range(0, len(sample), 32)]

        for c in range(256):
            char = hexlify(chr(c).encode("latin1"))
            guess = p.send(b"2", dummy + keyE + char)
            guess_block = [guess[i:i+32] for i in range(0, len(guess), 32)]
            if sample_block[1] == guess_block[1]:
                keyE += char
                break

        print("keyE ->", unhexlify(keyE))

    unhex_keyE = unhexlify(keyE)
    keyE = unhex_keyE[noise_len:]
    noise = unhex_keyE[:noise_len]

    # decrypt flag using aes3
    aes3 = AES.new(keyE, AES.MODE_ECB)
    cipher123 = aes3.decrypt(unhexlify(enc_flag))

    # setup known-plaintext attack
    known_plain = hexlify(b"A" * (64 - noise_len))
    known_cipher1234 = unhexlify(p.send(b"2", known_plain))
    known_cipher123 = aes3.decrypt(known_cipher1234)
    extended_plain = pad(unhexlify(known_plain) + noise + keyE, 16)

    # brute-force last 2 bytes
    keyB = b"v3rys3cur3pwd!"
    for i,j in permutations(range(256), 2):
        ij = (chr(i) + chr(j)).encode("latin1")
        key = keyB + ij

        # exec known-plaintext attack
        aes0 = AES.new(key, AES.MODE_CBC, iv=keyE)
        cipher1 = aes0.encrypt(extended_plain)
        guess_stream_key = xor(cipher1, known_cipher123)

        ac1 = xor(aes3.decrypt(unhexlify(enc_flag)), guess_stream_key)
        taes = AES.new(key, AES.MODE_CBC, iv=keyE)
        flag = taes.decrypt(ac1)
        if b"slashroot7" in flag:     # adjust depends on flag format
            print(flag)
finally:
    p.close()