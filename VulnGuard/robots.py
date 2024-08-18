import urllib.request
import ssl
import io
from urllib.parse import urlparse

def sanitize_url(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc or parsed_url.path

def get_robots_txt(url):
    domain = sanitize_url(url)
    path = f"https://{domain}/robots.txt"
    
    context = ssl._create_unverified_context()
    try:
        req = urllib.request.urlopen(path, context=context)
        data = io.TextIOWrapper(req, encoding='utf-8')
        return data.read()
    except:
        return None

def get_sitemap(url):
    domain = sanitize_url(url)
    sitemap_url = f"https://{domain}/sitemap.xml"
    try:
        req = urllib.request.urlopen(sitemap_url)
        data = io.TextIOWrapper(req, encoding='utf-8')
        return data.read()
    except:
        return None

def enumerate_hidden_paths(url):
    domain = sanitize_url(url)
    wordlist = ['admin', 'login', 'dashboard', 'config']
    paths = []
    for word in wordlist:
        test_url = f"https://{domain}/{word}"
        try:
            response = urllib.request.urlopen(test_url)
            if response.code == 200:
                paths.append(test_url)
        except:
            pass
    return paths
