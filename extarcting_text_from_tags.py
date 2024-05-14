import requests
from bs4 import BeautifulSoup
web=requests.get("https://www.tutorialsfreak.com/")
soup=BeautifulSoup(web.content,"html.parser")
lines=soup.find_all("p")
print(lines)
print("\n")
for l in lines:
    print(l.text)
print("\n")
s=soup.find("div",class_="why-choose-card card-shadow card")
line_1=s.find_all("p")
print(line_1)
print("\n")
for l1 in line_1:
    print(l1.text)