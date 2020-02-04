from  selenium import webdriver
import time,os
from bs4 import BeautifulSoup as BP
url="http://hahow.in/courses"
driver=webdriver.Chrome("chromedriver")
driver.implicitly_wait(2)
driver.get(url)
print(driver.title)
A=driver.find_elements_by_css_selector("h4.title")
for data in A:
    print(data.text)
B=driver.find_elements_by_class_name("wording")
for data in B:
    print(data.text)
driver.quit()
