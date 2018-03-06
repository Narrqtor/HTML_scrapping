#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

import re

website = requests.get("http://steamcommunity.com/id/stormstaticsleep/")

soup = BeautifulSoup(website.content, 'html.parser')

player_infos = []

name = soup.find(class_="actual_persona_name").get_text()
level = "Level " + soup.find(class_="friendPlayerLevel").get_text()
badge = "Favorite badge is " + soup.find(class_="name ellipsis").get_text()
country = soup.find(class_="profile_flag").get_text()
country_clean = re.sub(r'\s+', '', country)

player_infos.append(name)
player_infos.append(level)
player_infos.append(badge)
player_infos.append(country_clean)

for element in player_infos:
	print(element)

items = soup.find(class_="profile_item_links")
side_items = items.find_all(class_="profile_count_link ellipsis")

for stuff in side_items:
	stuff = re.sub(r'\s+', ' ', stuff.get_text())
	print (stuff[1:])

#print(soup.prettify())
