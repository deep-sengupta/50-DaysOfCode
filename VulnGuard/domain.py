import socket
import ssl
import requests
from urllib.parse import urlparse
import os

def get_domain_name(url):
    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc or parsed_url.path
    return domain_name

def get_reverse_dns(ip_address):
    try:
        return socket.gethostbyaddr(ip_address)[0]
    except socket.herror:
        return None

def get_geo_location(ip_address):
    response = requests.get(f"https://geolocation-db.com/json/{ip_address}&position=true").json()
    return response

def get_dns_records(url):
    domain = get_domain_name(url)
    command = f"dig {domain} ANY +short"
    process = os.popen(command)
    results = process.read().strip()
    return results

def get_ssl_certificate_info(url):
    domain = get_domain_name(url)
    context = ssl.create_default_context()
    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            cert = ssock.getpeercert()
    return cert
