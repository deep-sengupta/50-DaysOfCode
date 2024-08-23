<h1>Cipher</h1>
Cipher is a Python-based file encryption and decryption tool that secures your sensitive data using the Advanced Encryption Standard (AES) in GCM mode. The tool allows you to encrypt all files in a directory except the encryption and decryption scripts themselves. You can later decrypt these files using the same secret phrase.

## Prerequisites
```
pip install cryptography
```

## Usage
### Encryption
```
python3 encrypt.py
```
- Enter a secret phrase when prompted. This phrase will be used to generate the encryption key.
- The script will encrypt all files and save the key in a confidential.key file.
- Important: Keep the secret phrase safe. You will need it for decryption.

### Decryption
```
python3 decrypt.py
```
- Enter the same secret phrase you used during encryption.
- The script will decrypt the files if the correct phrase is provided.

## Important Notes
- `Backup`: Before running these scripts, ensure that you have backed up your data, as encryption is irreversible without the correct secret phrase.
- `Security`: Do not share your secret phrase or confidential.key file with anyone. If either is compromised, your files may be at risk.