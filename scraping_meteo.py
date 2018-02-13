#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

### Download the website you want to scrap from

website = requests.get("http://www.meteofrance.com/accueil")

### Parse it with BeautifulSoup

soup = BeautifulSoup(website.content, 'html.parser')

### Display the date by finding the tags you are looking for
### In my case, time

time = soup.find_all('time')
date = time[0].get_text()
print(date)

### Retrieve the data of the zone you want to retrieve the weather from

continent = soup.find_all('p')
print(continent)

