# DNS Verifier
This repository contains two scripts — one written in Python and another in Bash — that perform DNS resolution checks and return whether the DNS is available (i.e., no A records found) along with its resolved IP addresses.

## Overview
Both scripts take a DNS (domain name) as input and return:
- The provided DNS.
- The resolved IP addresses (if any).
- A flag indicating whether the DNS is available (`AVAIL: true` if no IPs are found, meaning the DNS doesn't resolve to any IP).

## Python Script

### Requirements
- Python 3.x
- `dnspython` library
```
pip3 install dnspython
```

### How to Run
- Run the Python script using the command below:
```
python3 main.py
```
- Enter the DNS name when prompted.

Example:
```
Enter the DNS:
example.com
{
    "DNS": "example.com",
    "IP": [
        "93.184.216.34"
    ],
    "AVAIL": false
}
```

## Bash Script
### How to Run
- Make the Bash script executable:
```
chmod +x dns.sh
```
- Run the script using the command below:
```
./dns.sh
```
Example:
```
Enter the DNS:
example.com
{
    "DNS": "example.com",
    "IP": "93.184.216.34",
    "AVAIL": false
}
```