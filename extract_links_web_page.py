import requests
from bs4 import BeautifulSoup
web=requests.get("https://www.tutorialsfreak.com/")
soup=BeautifulSoup(web.content,"html.parser")
# print(soup.find_all("a"))
for i in soup.find_all("a"):
    print(i.get("href"))