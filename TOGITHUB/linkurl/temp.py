import webbrowser
url="https://www.google.com.tw/maps/place/"
adr=input("地址: ")
webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url+adr)
#webbrowser.open(url+adr, new=0, autoraise=True)#IE