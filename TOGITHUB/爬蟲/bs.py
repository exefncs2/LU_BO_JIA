htm='''<html><head><title>國立臺灣大學系統</title></head>
<body>
<p class="title"><b>三校聯盟 NTU SYSTEM</b></p>
<p class="ntu_system">
<a href="http://www.ntu.edu.tw" class="union" id="link1">臺灣大學</a>
<a href="http://www.ntnu.edu.tw" class="union" id="link2">臺灣師範大學</a>
<a href="http://www.ntust.edu.tw" class="union" id="link3">臺灣科技大學</a>
</p></body></html>
'''

from bs4 import BeautifulSoup as BS
soup=BS(htm,"html.parser")
A1=soup.title
A2=soup.find("a")#<a>
A3=soup.find("b")#<b>
A4=soup.find_all("a",{"class":"union"})
web=soup.find("a",{"id":"link1"})
data=soup.select(".union")#list[]
B=soup.select("#link3")#list[]
print(A1)
print("*"*50)
print(A2)
print("*"*50)
print(A3)
print("*"*50)
print(A4)
print("*"*50)
print(web.get("href"))#常用GET網址
print("*"*50)
for i in data:
    print(i)#data[0~n]
print("*"*50)
print(B)
print("*"*50)   



    
print("   --------------------ALL----------------------")
print("*"*50)   
print(soup)