#!/usr/bin/env python3

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend

with open("confidential.key", "rb") as key_file:
    salt = key_file.read(16)
    key = key_file.read()

user_phrase = input("Enter the secret phrase to decrypt your files: ").encode()

kdf = Scrypt(
    salt=salt,
    length=32,
    n=2**14,
    r=8,
    p=1,
    backend=default_backend()
)
try:
    derived_key = kdf.derive(user_phrase)
except:
    print("Wrong secret phrase, you can't decrypt your files.")
    exit()

if derived_key != key:
    print("Wrong secret phrase, you can't decrypt your files.")
    exit()

files = []

for file in os.listdir():
    if file in ("encrypt.py", "confidential.key", "decrypt.py"):
        continue
    if os.path.isfile(file):
        files.append(file)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()

    iv = contents[:12]
    tag = contents[12:28]
    ciphertext = contents[28:]

    decryptor = Cipher(
        algorithms.AES(derived_key),
        modes.GCM(iv, tag),
        backend=default_backend()
    ).decryptor()
    contents_decrypted = decryptor.update(ciphertext) + decryptor.finalize()

    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)

print("Congrats, your files are decrypted.")
