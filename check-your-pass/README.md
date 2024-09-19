# Password Breach and Strength Checker

This Python script allows you to check whether a password has been compromised using the [Have I Been Pwned API](https://haveibeenpwned.com/API/v3). It also evaluates the strength of the password based on common security criteria.

## Features
- **Check Password Breaches:** Determines if your password has been found in any data breaches.
- **Evaluate Password Strength:** Provides a rating of the password's strength (Weak, Moderate, or Strong).

## Requirements
To use this script, you need the following dependencies installed:

- Python 3.x
- `requests` library
```bash
pip install requests
```

## How It Works
- The script hashes the password using the SHA-1 algorithm.
- It sends the first 5 characters of the hashed password to the Have I Been Pwned API.
- The API returns a list of matching hashes, and the script checks if the full hash of the password is in the list.
- The script also checks the strength of the password based on:
  - Password length
  - Combination of lowercase, uppercase, and numeric characters

## Example
```
python3 main.py mypassword1
```
Output:
```
mypassword1: Found 3500 times, consider changing it.
Strength: Weak
```