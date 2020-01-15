# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 09:10:37 2020

@author: ASUS
"""

import requests
url=input("網址:")
http=requests.get(url)
http.encoding="utf-8"
http_list=http.text.splitlines()
n=0
#lows=[]
c=0
key=input("搜尋:")
for low in http_list:
    c+=1
    if key in low:
        n+=1
       #lows.append(low) 
        print("找到{}在{}行".format(key,c))
    for word in low:
        if key in word:
            print("找到{}在{}行".format(key,c))
        
print("{}在內容中有{}個".format(key,n))


