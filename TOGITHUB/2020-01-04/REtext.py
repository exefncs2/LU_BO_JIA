import re
import requests
from bs4 import BeautifulSoup
#A=input("電子郵件:")
#patn=re.compile("@.+.")
#print(patn.findall(A))
url="https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5"
req=requests.get(url)
soup= BeautifulSoup(req.text,"html.parser")
titles=soup.find_all(re.compile("h[1-6]"))#["h1","h2","h3","h4","h5","h6"]
for title in titles:
    print(title.text.strip())
print("*"*50,2)
imgs=soup.find_all('img')
for img in imgs:
    if "src" in img.attrs:#attrs
        if img['src'].endswith(".png"):
            print(img["src"])
#
print("*"*50,3)
for img in soup.find_all("img",{"src":re.compile(".png$")}):
    print(img["src"])