import hashlib
import sys
import pyfiglet
import time

ascii_banner = pyfiglet.figlet_format("UnHash")
print(ascii_banner)

print("Algorithms available: MD5 | SHA1 | SHA224 | SHA512 | SHA384")

hash_type = str(input("Enter the hash type: "))
wordlist_location = str(input("Enter the wordlist location: "))
hash = str(input("Enter the hash: "))

start_time = time.time()

try:
    word_list = open(f"{wordlist_location}", encoding="ISO-8859-1").read()
    lists = word_list.splitlines()
except FileNotFoundError:
    print("\033[1;31m ERROR: Wordlist file not found. Please check the file location and try again.")
    sys.exit(1)
except Exception as e:
    print(f"\033[1;31m ERROR: {e}")
    sys.exit(1)

print("\033[1;34m Starting to crack the hash...\n")

found = False
for word in lists:
    if hash_type == "MD5":
        hash_object = hashlib.md5(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
    elif hash_type == "SHA1":
        hash_object = hashlib.sha1(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
    elif hash_type == "SHA224":
        hash_object = hashlib.sha224(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
    elif hash_type == "SHA512":
        hash_object = hashlib.sha512(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
    elif hash_type == "SHA384":
        hash_object = hashlib.sha384(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
    else:
        print("\033[1;31m ERROR: Invalid hash type. Please choose from the given options.")
        sys.exit(1)

    if hash == hashed:
        print(f"\033[1;32m HASH FOUND: {word} \n")
        found = True
        break

if not found:
    print("\033[1;31m ERROR: Hash not found in the wordlist. Please try a different wordlist.")

end_time = time.time()
duration = end_time - start_time
print(f"\033[1;34m Time taken: {duration:.2f} seconds")

print("\033[1;34m Finished searching through the wordlist.")