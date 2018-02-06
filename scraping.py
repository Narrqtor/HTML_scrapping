import urllib2
from bs4 import BeautifulSoup

url_page = 'https://www.facebook.com'
page = urllib2.urlopen(url_page)
soup = BeautifulSoup(page, 'html.parser")

