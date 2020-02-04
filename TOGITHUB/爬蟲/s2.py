import requests
from bs4 import BeautifulSoup
import os,urllib

url="https://technews.tw/2020/01/30/no-evidence-shows-that-pets-can-also-get-wuhan-pneumonia/"
html=requests.get(url)
html.encoding="utf-8"
bs=BeautifulSoup(html.text,"html.parser")

if not os.path.exists("pics"):
    os.mkdir("pics")
all_img=bs.find_all("img")
for link in all_img:
    src=link.get("src")
    attrs=[src]
    for attr in attrs:
        if attr!=None and (".jpg" in attr or ".png" in attr):
            full_path=attr
            file_n=full_path.split("/")[-1]#尾端
            print("完整路徑:",end=" ")
            print(full_path)
            try:
                image =urllib.request.urlopen(full_path)
                f=open(os.path.join("pics",file_n),"wb")
                f.write(image.read())
                print("下載成功, %s" %(file_n))
                f.close()
            except:
                print("error %s not find" %(file_n))