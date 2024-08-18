import os
from urllib.parse import urlparse

def sanitize_url(url):
    return urlparse(url).netloc or urlparse(url).path

def get_whois(url):
    domain_or_ip = sanitize_url(url)
    command = f"whois {domain_or_ip}"
    process = os.popen(command)
    results = str(process.read())
    return results

def parse_whois_data(raw_data):
    parsed_data = {}
    lines = raw_data.splitlines()
    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            parsed_data[key.strip()] = value.strip()
    return parsed_data

def get_advanced_whois(url):
    whois_data = get_whois(url)
    parsed_data = parse_whois_data(whois_data)
    return parsed_data

def get_historical_whois(url):
    domain_or_ip = sanitize_url(url)
    command = f"whois-history {domain_or_ip}"
    process = os.popen(command)
    results = str(process.read())
    return results
