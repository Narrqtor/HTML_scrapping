#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

import pandas

import re

class ScrapingWeb():
	"""Doc for ScrapingWeb"""
	"""website is the variablae that stores the URL"""
	"""webpage stores the HTML content once the request was made with requests.get()"""
	"""frame is the value we check for frame display"""
	"""list is the value we check for value display"""
	
	def __init__(self):
		self.website = ""
		self.webpage = ""
		self.frame = False
		self.list = False

	def retrieveWebsite(self):
		print("What website would you like to scrap from ?\n")
		self.website = input()

	def checkWebsite(self):
		try:
			self.webpage = requests.get(self.website)
		except:
			print("Are you sure this is a valid website ?\n")
			ScrapingWeb().retrieveWebsite(self)
			return

	def displayInfo(self):
		print("What display would you like to see ?\n[F]rame or [L]ist: ", end='')
		answer = input()
		if answer[0] == "F" or answer[0] == "f":
			self.frame = True
		elif answer[0] == "L" or answer[0] =="l":
			self.list = True
		elif answer == "quit":
			sys.exit()
		else:
			print("Sorry, this is not a correct answer.\n")
			self.displayInfo()
			return

	def scrapingMeteo(self):
		website = requests.get("http://www.meteofrance.com/accueil") ### Download the website you want to scrap from
		soup = BeautifulSoup(website.content, 'html.parser') ### Parse it with BeautifulSoup
		time = soup.find_all('time') ### Display the date by finding the tags you are looking for
		date = time[0].get_text()
		print(date)
		france = soup.find(class_="tableToMap carte carte-pays007") ### Retrieve the data of the zone you want to retrieve the weather from
		forecast_items = france.find_all(class_="pictoMap")
		self.displayInfo()

		if self.frame == True:
			A=[] # You can create a data frame and put your information in it.
			B=[]
			for stuff in forecast_items:
				cells = stuff.find(class_="picTemps").get_text()
				states = stuff.find(class_="temper celsiusUnit").get_text()
				places = re.sub(r'METEO', '', cells)
				places = re.sub(r'\s+', ' ',places)
				A.append(places)
				B.append(states+"°C")
			df=pandas.DataFrame(A,columns=['Lieux'])
			df['Températures']=B
			print(df)

		if self.list == True:
			for infos in forecast_items: # Loop over the list you have and retrieve the information you are looking for.
				location = infos.find(class_="picTemps").get_text()
				units = infos.find(class_="temper celsiusUnit").get_text()
				lo = re.sub(r'METEO', '', location)
				lo = re.sub(r'\s+', ' ', lo)
				print(lo[1:])
				print("Il y fait",units, "degrés Celsius.\n")


def main():
	scrapingObj = ScrapingWeb()
	scrapingObj.scrapingMeteo()
	return

if __name__ == '__main__':
	main()
