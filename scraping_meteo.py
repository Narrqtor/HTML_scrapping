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

france = soup.find(class_="tableToMap carte carte-pays007")
forecast_items = france.find_all(class_="pictoMap")
text = forecast_items

#print(text.prettify())

# Loop over the list you have and retrieve the information you are looking for.

for infos in forecast_items:
	location = infos.find(class_="picTemps")
	units = infos.find(class_="temper celsiusUnit")
	print(location.get_text())
	print(units.get_text())

### ALso works with the following, but depends on the website

#	print(infos.get_text())
