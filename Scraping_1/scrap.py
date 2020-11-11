from six.moves import urllib
from bs4 import BeautifulSoup

datos = urllib.request.urlopen("https://www.youtube.com/playlist?list=PLBdkl5-ytBTwBjlnOh_rOcLy1NlFQ4Q4Q").read().decode('utf-8')

soup =  BeautifulSoup(datos, 'lxml')
tags = soup("a")

for tag in tags:
	print(tag.get("href"))