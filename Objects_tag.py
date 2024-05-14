import requests
from bs4 import BeautifulSoup
web=requests.get("https://www.tutorialsfreak.com/")
soup=BeautifulSoup(web.content,"html.parser")
# TAG
tag=soup.html
print(type(tag))
tag=soup.p
print(tag)
tag=soup.a
print(tag)