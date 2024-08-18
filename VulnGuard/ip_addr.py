import os
import socket
import requests
from urllib.parse import urlparse

def get_ip_address(url):
    domain = urlparse(url).netloc or urlparse(url).path
    command  = f"host {domain}"
    process = os.popen(command)
    results = str(process.read())
    marker = results.find('has address') + 12
    ip_address = results[marker:].splitlines()[0]
    return ip_address

def get_ip_owner(ip_address):
    command = f"whois {ip_address}"
    process = os.popen(command)
    results = str(process.read())
    owner_info = ""
    for line in results.splitlines():
        if "OrgName" in line or "netname" in line:
            owner_info += line + "\n"
    return owner_info

def get_subnet(ip_address):
    try:
        ip_obj = socket.gethostbyname_ex(ip_address)
        return ip_obj[-1]
    except socket.error:
        return None

def get_asn_info(ip_address):
    response = requests.get(f"https://api.hackertarget.com/aslookup/?q={ip_address}")
    return response.text

def check_ip_reputation(ip_address):
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    reputation = response.json().get("threat", "No threat data available")
    return reputation
