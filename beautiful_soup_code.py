import requests


import requests
from bs4 import BeautifulSoup
url='https://www.google.com/'
r=requests.get(url)
htmlcontent = r.content
soup= BeautifulSoup(r.content,'html.parser')
print(soup.prettify())