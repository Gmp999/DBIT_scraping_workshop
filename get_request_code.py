import requests
url='https://www.google.com/'
r=requests.get(url)
htmlcontent= r.content
print(htmlcontent)
