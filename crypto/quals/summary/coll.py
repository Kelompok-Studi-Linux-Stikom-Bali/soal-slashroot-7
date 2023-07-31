import hashlib

def sha1sum(b: bytes):
    return hashlib.sha1(b).digest()[:3]

whitelisted_cmd = b'echo lol'
whitelisted_hash = sha1sum(whitelisted_cmd)

print(whitelisted_hash)

coll = b''

for i in range(2**80):
    print((f"echo {i:010} | cat *").encode())
    if whitelisted_hash == sha1sum((f"echo {i:010} | cat *").encode()):
        coll = (f"echo {i:010} | cat *").encode()
        break

print(f"Collition Found at : {coll.decode()}")