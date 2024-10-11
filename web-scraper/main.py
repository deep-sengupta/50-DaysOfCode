import requests
from bs4 import BeautifulSoup

url = input("Enter the URL: ")
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

urls = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href:
        urls.append(href)

with open('results.txt', 'w') as file:
    for url in urls:
        file.write(f"{url}\n")

print(f"Results have been saved in results.txt")
