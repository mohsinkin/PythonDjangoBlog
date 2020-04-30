from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome(executable_path=r'C:\Users\mohsi.MOSSOSAURUSPC\Downloads\chromedriver.exe')

driver.get('https://moss-blog.herokuapp.com')
print(driver.title)

driver.get('http://google.com')
print(driver.title)

driver.back()
print(driver.title)

driver.forward()
print(driver.title)

driver.close()