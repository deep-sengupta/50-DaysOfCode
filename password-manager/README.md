# LockBox Password Manager
LockBox is a command-line-based password manager that helps you securely store, retrieve, and manage your passwords. It uses AES-256 encryption to protect your data and offers a simple interface to handle your credentials.

## Features
- `Secure Encryption`: Uses AES-256 encryption to store passwords securely.
- `Master Password`: Protects access to your stored passwords with a master password. Users can create a new master password or log in with an existing one.
- `Retrieve Passwords`: Easily retrieve passwords for your saved applications.
- `Save New Passwords`: Add new passwords for different applications.
- `Delete Passwords`: Remove passwords for applications you no longer use.
- `Change Master Password`: Update your master password at any time.

## Usage
- Dependencies include:
`Python3`
```
pip3 install pyfiglet pycryptodome
```
- Run the Application:
```
python3 main.py
```
- If running for the first time, create a master password to secure your passwords.
- If already set, enter your master password to access the password manager.

## Security Notes
- The master password is encrypted and stored locally in a file. Ensure this file remains secure and do not share it.
- Your passwords are encrypted using AES-256, but it is crucial to use a strong and unique master password to maintain security.