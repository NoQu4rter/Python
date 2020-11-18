from six.moves import urllib
from bs4 import BeautifulSoup
import re

datos = urllib.request.urlopen("https://www.youtube.com/playlist?list=PL0ONFXpPDe_mtm3ciwL-v7EE-7yLHDlP8").read().decode('utf-8')

soup = BeautifulSoup(datos, 'lxml')

tag = soup.find_all('script')[26]

data = re.search(".\"text\":\"[0-9]+\".,.\"text\":\" videos\".", tag.string)

if data:
	data = re.search('[0-9]+', data.group(0))
	print(data.group(0))

# {"text":"11"},{"text":" videos"}