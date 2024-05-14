import requests
from bs4 import BeautifulSoup
web=requests.get("https://www.tutorialsfreak.com/")
soup=BeautifulSoup(web.content,"html.parser")
print(soup.prettify())
print("\n")
class_data=soup.find("div",class_="bg-white border-0 p-3 card-footer")
# for id just use id=
print(class_data.prettify())