url="https://tw.appledaily.com/daily/"
import requests

from bs4 import BeautifulSoup
apple=requests.get(url).text
soup=BeautifulSoup(apple,"html.parser")
number=0
print("-------------------------------------------頭條----------------------------------------")
for i in soup.find("ul","fillup").find_all("li"):
    number+=1
    print(str(number)+". "+ i.find("a").get("title"))
print("--------------------------要聞------------------------------------")
number2=0
x=[]
for i in soup.find_all('article','nclns eclnms5'):

    for j in i.find_all("li"):
        number2 += 1
        if j.get("title")!="":
             print(str(number2)+". "+ j.find("a").get("title"))
