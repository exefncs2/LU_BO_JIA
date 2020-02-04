import requests
from bs4 import BeautifulSoup

url="https://www.taiwanlottery.com.tw/index_new.aspx"
html=requests.get(url)
bs=BeautifulSoup(html.text,"html.parser")

data1=bs.select(".contents_box02")
time=data1[0].find("span","font_black15").text
data2=data1[0].find_all("div",{"class":"ball_tx"})
data3=bs.select(".contents_box04")
time2=data3[1].find("span","font_black15").text
data4=data3[1].find_all("div",{"class":"ball_tx"})

print("----------ALL----data---------------")
print(data1)
print("--------49------------------")
print(data2)
print("----------時間---------------")
print(("{}").format(time))
print("-----整理49-----------")
for n in range(6):
    print(data2[n].text,end=" ")
print()
print("----時間2-----(4星)----")
print(("{}").format(time2))
print("-----整理4星---------")
for n in range(4):
    print(data4[n].text,end=" ")