import json
import sys
from collections import OrderedDict
import dns.resolver
import socket

def checker(dns_val=None) -> OrderedDict:
    if not dns_val:
        raise ValueError("DNS is required")
    if not isinstance(dns_val, str):
        raise TypeError("DNS must be a string")

    ip_values, avail = [], False
    resolver = dns.resolver.Resolver()
    resolver.lifetime = 5
    resolver.timeout = 5

    try:
        output = resolver.resolve(dns_val, 'A')
        ip_values = [ipval.to_text() for ipval in output]
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.NoNameservers):
        avail = True
    except (dns.resolver.Timeout, socket.gaierror):
        raise RuntimeError("DNS resolution timed out or failed")

    return OrderedDict([
        ("DNS", dns_val),
        ("IP", ip_values),
        ("AVAIL", avail),
    ])

if __name__ == '__main__':
    dns_val = input("Enter the DNS: ")
    try:
        response = checker(dns_val=dns_val)
        print(json.dumps(response, indent=4))
    except Exception as err:
        print(f"Error: {err}")
        sys.exit(1)
    sys.exit(0)