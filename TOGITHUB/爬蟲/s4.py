from  selenium import webdriver
import time,os
from bs4 import BeautifulSoup as BP
url="http://hahow.in/courses"
driver=webdriver.Chrome("chromedriver")
#driver.implicitly_wait(20)
driver.get(url)
print(driver.title)

soup=BP(driver.page_source,"lxml")
fp=open("hahow.html","w",encoding="utf8")
fp.write(soup.prettify())
print("OK")
fp.close()
driver.quit()
