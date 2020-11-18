from six.moves import urllib
from bs4 import BeautifulSoup
import json
import re

datos = urllib.request.urlopen("https://www.youtube.com/playlist?list=PLBdkl5-ytBTwBjlnOh_rOcLy1NlFQ4Q4Q").read().decode('utf-8')

#k = 0

soup = BeautifulSoup(datos, 'lxml')

tag = soup.find_all('script')[26]

data = re.search(".\"text\":\"11\".,.\"text\":\" videos\".", str(tag))

print(data)

#for tag in soup.find_all('script'):
#
#	k = k + 1
#
#	k = str(k)
#
#	print "[ETIQUETA " + k + "]"
#	print (tag)
#	k = int(k)

#print ( soup.find(id="stats") )

# "stats":[{"runs":[{"text":"11"},{"text":" videos"}]}
# {"runs":[{"text":"11"},{"text":" videos"}]}
# {"text":"11"},{"text":" videos"}