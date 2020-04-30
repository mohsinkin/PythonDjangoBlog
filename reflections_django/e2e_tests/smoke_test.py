from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome(executable_path=r'C:\Users\mohsi.MOSSOSAURUSPC\Downloads\chromedriver.exe')

driver.get('https://moss-blog.herokuapp.com/login')
print(driver.title)

user_name_elem = driver.find_element_by_name('username')
password_elem = driver.find_element_by_name('password')
submit_button = driver.find_element_by_css_selector('button.btn-outline-info')
# print(user_name_elem.is_displayed())
# print(user_name_elem.is_enabled())
# print(password_elem.is_displayed())
# print(password_elem.is_enabled())

user_name_elem.send_keys('test_headless')
password_elem.send_keys('Testing!@')
submit_button.click()


driver.close()
driver.quit()