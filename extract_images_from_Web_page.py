import requests
from bs4 import BeautifulSoup
web=requests.get("https://www.tutorialsfreak.com/")
soup=BeautifulSoup(web.content,"html.parser")
image=soup.find_all("img")
for i in image:
    print(i.get("src"))
    # print(i.get("alt"))