import requests
r=requests.get("https://www.facebook.com/petpetplaza/")
print(r.status_code)
r.encoding="utf-8"
data=r.text
#data=r.json()
#for i in range(len(data)):
 #   for j in data[i]:
 #      print(j)
 # 目標為json使用
print(data)