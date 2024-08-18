from general_utils import *
from domain import *
from ip_addr import *
from netscan import *
from robots import *
from whois import *

ROOT_DIR = 'Results'
create_dir(ROOT_DIR)

def gather_info(name, url):
    domain = get_domain_name(url)
    ip_addr = get_ip_address(url)
    netscan = get_nmap('-F', ip_addr)
    robots = get_robots_txt(url)
    whois = get_whois(domain)
    create_report(name, url, domain, netscan, robots, whois)

def create_report(name, full_url, domain, netscan, robots, whois):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/full_url.txt', full_url)
    write_file(project_dir + '/domain_name.txt', domain)
    write_file(project_dir + '/netscan.txt', netscan)
    write_file(project_dir + '/robots.txt', robots)
    write_file(project_dir + '/whois.txt', whois)

if __name__ == "__main__":
    name = input("Enter the project name: ")
    url = input("Enter the URL to scan: ")
    gather_info(name, url)
