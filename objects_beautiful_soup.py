import requests
from bs4 import BeautifulSoup
web=requests.get("https://www.tutorialsfreak.com/")
soup=BeautifulSoup(web.content,"html.parser")
print(soup.title)
print(soup.body)
# find function
print("\n")
print(soup.find("p"))
# to find all
print("\n")
print(soup.find_all("p"))