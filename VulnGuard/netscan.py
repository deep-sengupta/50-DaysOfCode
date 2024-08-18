import os
from urllib.parse import urlparse

def sanitize_url(url):
    parsed_url = urlparse(url)
    domain_or_ip = parsed_url.netloc or parsed_url.path
    return domain_or_ip

def get_nmap(options, url):
    domain_or_ip = sanitize_url(url)
    command = f"nmap {options} {domain_or_ip}"
    process = os.popen(command)
    results = process.read().strip()
    return results

def deep_nmap_scan(url):
    domain_or_ip = sanitize_url(url)
    command = f"nmap -A -sV -sC {domain_or_ip}"
    process = os.popen(command)
    results = process.read().strip()
    return results

def vulnerability_scan(url):
    domain_or_ip = sanitize_url(url)
    command = f"nmap --script vuln {domain_or_ip}"
    process = os.popen(command)
    results = process.read().strip()
    return results

def banner_grabbing(url, port):
    domain_or_ip = sanitize_url(url)
    command = f"nc -v -n -w 1 {domain_or_ip} {port}"
    process = os.popen(command)
    results = process.read().strip()
    return results
