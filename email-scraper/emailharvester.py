import requests
import re
import time
from bs4 import BeautifulSoup

emailRegex = re.compile(r'''
                        (
                        ([a-zA-Z0-9_.+]+
                        @
                        [a-zA-Z0-9_.+]+)
                        )
                        ''', re.VERBOSE)

def extractEmailFromUrlText(urlText):
    extractedEmail = emailRegex.findall(urlText)
    allemails = []
    for email in extractedEmail:
        allemails.append(email[0])
    lenh = len(allemails)
    print("\tNumber of Emails: %s\n" % lenh)
    seen = set()
    for email in allemails:
        if email not in seen:
            seen.add(email)
            emailFile.write(email + "\n")

def htmlPageRead(url, i):
    try:
        start = time.time()
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        urlText = soup.get_text()
        print("%s.%s\tFetched in: %s seconds" % (i, url, (time.time() - start)))
        extractEmailFromUrlText(urlText)
    except Exception as e:
        print(f"Failed to read {url}: {e}")
        pass

def emailsLeechFunc(url, i):
    try:
        htmlPageRead(url, i)
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 404:
            try:
                cache_url = 'http://webcache.googleusercontent.com/search?q=cache:' + url
                htmlPageRead(cache_url, i)
            except Exception as e:
                print(f"Failed to fetch from cache for {url}: {e}")
                pass
        else:
            print(f"HTTP Error: {err.response.status_code} for {url}")
            pass

start = time.time()
urlFile = open("urls.txt", 'r')
emailFile = open("emails.txt", 'a')
i = 0

for urlLink in urlFile.readlines():
    urlLink = urlLink.strip('\'"')
    i = i + 1
    emailsLeechFunc(urlLink, i)

print("Elapsed Time: %s seconds" % (time.time() - start))

urlFile.close()
emailFile.close()
