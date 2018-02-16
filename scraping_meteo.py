#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

import pandas

import re 

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

#print(text.prettify())

# You can create a data frame and put your information in it.
# Loop over the list you just got

A=[]
B=[]

for stuff in forecast_items:
	cells = stuff.find(class_="picTemps").get_text()
	states = stuff.find(class_="temper celsiusUnit").get_text()
	places = re.sub(r'METEO', '', cells)
	places = re.sub(r'\s+', ' ', places)
	A.append(places)
	B.append(states)

df=pandas.DataFrame(A,columns=['Lieux'])
df['Températures']=B
print(df)

print('\n')  # For a neater display
print('\n')  # For a neater display

# Loop over the list you have and retrieve the information you are looking for.

for infos in forecast_items:
	location = infos.find(class_="picTemps").get_text()
	units = infos.find(class_="temper celsiusUnit").get_text()
	lo = re.sub(r'METEO', '', location)
	lo = re.sub(r'\s+', ' ', lo)
	print(lo)
	print("Il y fait ",units, " degrés Celsius.\n")

### Also works with the following, but depends on the website

#	print(infos.get_text())
