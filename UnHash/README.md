# UnHash - Hash Cracking Tool
UnHash is a Python-based hash cracking tool that supports multiple hashing algorithms. It's designed to help in security testing and password recovery by checking hashes against a list of potential plaintext passwords.

## Features
### Supported Algorithms:

- `MD5` `SHA1` `SHA224` `SHA384` `SHA512`
- `Custom Wordlist`: You can provide your own wordlist for cracking.
- `Simple Interface`: Easy to use, with clear prompts for user input.

## Usage
- Run the script:
```
python unhash.py
```
- Enter the hash type: `MD5` `SHA1` `SHA224` `SHA384` `SHA512`
- Provide the wordlist location: `/path/to/wordlist.txt`
- Enter the hash to crack.

### Example
```
python unhash.py

Algorithms available: MD5 | SHA1 | SHA224 | SHA512 | SHA384
Enter the hash type: MD5
Enter the wordlist location: /path/to/wordlist.txt
Enter the hash: 5f4dcc3b5aa765d61d8327deb882cf99
Starting to crack the hash...

HASH FOUND: password 

Time taken: 0.23 seconds
Finished searching through the wordlist.
```