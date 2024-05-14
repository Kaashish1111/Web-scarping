import requests
from bs4 import BeautifulSoup
web=requests.get("https://www.tutorialsfreak.com/")
soup=BeautifulSoup(web.content,"html.parser")
# TAG
tag=soup.html
print(type(tag))
#  NAVIGABLE STRING
#  It helps us to get the string in between the tag
tag=soup.p.string
print(tag)