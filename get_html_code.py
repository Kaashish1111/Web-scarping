import requests
web=requests.get("https://www.tutorialsfreak.com/")
print(web)
print(web.content)
print("\n")  # \n for one line gap
print(web.url)
print(web.status_code)