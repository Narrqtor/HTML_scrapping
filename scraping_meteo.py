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

france = soup.find(id="map-forecast")
forecast_items = france.find_all(class_="tableToMap")
text = forecast_items[0]

#print(text.prettify())

# Loop over the list you have and retrieve the information you are looking for.

for infos in text:
	location = text.find_all(class_="picTemps")
	temp = text.find_all(class_="temper celsiusUnit")
	for places, units in zip(location, temp):
		print(places.get_text(), "il y fait ", units.get_text(), " degrés")
