# VulnGuard: Website Scanner
This project is a Python-based website scanner that provides various tools for analyzing websites. The scanner includes functionality for scanning domain names, general utilities, WHOIS information, IP addresses, network scanning, and fetching robots.txt files.

## Prerequisites
Before running the scanner, ensure you have the following installed:
    Python3
    Required Python libraries (listed in requirements.txt)

## Install or Update Python Certificates
### Windows:

- Install/Update Certificates:
```
python -m pip install --upgrade certifi
```
- You may need to set the SSL_CERT_FILE environment variable to the path of the cacert.pem file:
```
set SSL_CERT_FILE=C:\path\to\cacert.pem
```

### MacOS/Linux:

- Install/Update Certificates:
```
/Applications/Python\ 3.x/Install\ Certificates.command
```
```
sudo apt-get install --reinstall ca-certificates
OR
python -m pip install --upgrade certifi
```

## Usage
```
python main.py
```