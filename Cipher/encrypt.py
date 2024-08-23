#!/usr/bin/env python3

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from base64 import urlsafe_b64encode, urlsafe_b64decode
import os

salt = os.urandom(16)
backend = default_backend()

secret_phrase = input("Enter a secret phrase: ").encode()

kdf = Scrypt(
    salt=salt,
    length=32,
    n=2**14,
    r=8,
    p=1,
    backend=backend
)
key = kdf.derive(secret_phrase)

files = []

for file in os.listdir():
    if file in ("encrypt.py", "confidential.key", "decrypt.py"):
        continue
    if os.path.isfile(file):
        files.append(file)

with open("confidential.key", "wb") as key_file:
    key_file.write(salt + key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()

    iv = os.urandom(12)
    encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
        backend=backend
    ).encryptor()
    contents_encrypted = encryptor.update(contents) + encryptor.finalize()
    encrypted_data = iv + encryptor.tag + contents_encrypted

    with open(file, "wb") as thefile:
        thefile.write(encrypted_data)

print("All files have been encrypted. Keep your secret phrase safe!")
