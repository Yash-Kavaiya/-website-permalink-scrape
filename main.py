import requests
from bs4 import BeautifulSoup
import csv

# URL of the website https://class10it.blogspot.com/

url = input("https://class10it.blogspot.com/")

import requests
from bs4 import BeautifulSoup

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

# Find all <a> in your HTML that have a not null 'href'. Keep only 'href'.
links = [a["href"] for a in soup.find_all("a", href=True)]
print(links)
import requests
from bs4 import BeautifulSoup

def get_all_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for a_tag in soup.find_all('a'):
        href = a_tag['href']
    if href and href.startswith('https://class10it.blogspot.com/'):
        links.append(href)
    return links

url = 'https://class10it.blogspot.com/'
links = get_all_links(url)
for link in links:
    print(link)