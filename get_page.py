#import librarys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chromrdriver = "/home/chromedriver"
os.environ["webdriver.chrome.driver"] = chromrdriver
driver = webdriver.Chrome(chromrdriver)
driver.get("https://nan.ac/SearchPage?Entity=Need")

ScrollNumber = 2000
for i in range(1,ScrollNumber):
    driver.execute_script("window.scrollTo(1,50000)")
    print(f"{i + 1} ---->sucess")
    time.sleep(10)

file = open('/home/alireza/Desktop/alireza/web scraping/index.html', 'w')
file.write(driver.page_source)
file.close()

driver.close()
