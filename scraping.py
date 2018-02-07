#!/usr/local/sbin/python3

import requests
from bs4 import BeautifulSoup

website = requests.get("https://github.com/Narrqtor")

soup = BeautifulSoup(website.content, 'html.parser')
print(soup.find_all('p'))

print([type(item) for item in list(soup.children)])
html = list(soup.children)[3]
