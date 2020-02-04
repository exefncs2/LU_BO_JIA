from  selenium import webdriver
import time,os
from bs4 import BeautifulSoup as BP
url=os.path.abspath("SeleniumTest.html")
driver=webdriver.Chrome("chromedriver")
driver.implicitly_wait(10)
driver.get(url)
print(driver.title)
h3=driver.find_element_by_tag_name("h3")
print(h3.text)
p=driver.find_element_by_tag_name("p")
print(p.text)
content=driver.find_element_by_class_name("content")
print(content.text)
driver.quit()
