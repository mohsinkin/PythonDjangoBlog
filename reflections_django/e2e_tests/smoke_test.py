from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(
    executable_path=r"C:\Users\mohsi.MOSSOSAURUSPC\Downloads\chromedriver.exe"
)

# driver.get("https://moss-blog.herokuapp.com/login")
# driver.get('http://newtours.demoaut.com')
# driver.get('https://fs27.formsite.com/JWbzg8/dl7ji2h34f/index.html?1588373590273')
driver.get('http://testautomationpractice.blogspot.com')

# print(driver.title)

# user_name_elem = driver.find_element_by_name("username")
# password_elem = driver.find_element_by_name("password")
# submit_button = driver.find_element_by_id("login_button")
# # print(user_name_elem.is_displayed())
# # print(user_name_elem.is_enabled())
# # print(password_elem.is_displayed())
# # print(password_elem.is_enabled())

# user_name_elem.send_keys("test_headless")
# password_elem.send_keys("Testing!@")
# submit_button.click()

# create_post = driver.find_element_by_id("create")
# create_post.click()

# title_box = driver.find_element_by_name("title")
# content = driver.find_element_by_name("content")
# post_button = driver.find_element_by_css_selector("button.btn-outline-info")

# title_box.send_keys("Test Title")
# content.send_keys("Test Content")
# post_button.click()

# # Dropdown operations
# drop_down = Select(driver.find_element_by_id('RESULT_RadioButton-4'))
# #select by value
# # drop_down.select_by_value('5-10')

# #select by visible text
# drop_down.select_by_visible_text('5-10')
# for option in drop_down.options:
#     print(option.text)
# time.sleep(3)

alert_button = driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button')
alert_button.click()
driver.switch_to.alert.dismiss()

time.sleep(3)

driver.close()
driver.quit()
