import requests
from bs4 import BeautifulSoup
web=requests.get("https://www.tutorialsfreak.com/")
# print(web.content)
soup=BeautifulSoup(web.content,"html.parser") # created an object
print(soup.prettify())
print("\n")
print(soup.title)
print("\n")
print(soup.p)
print("\n")
print(soup.a)
print(soup.img)