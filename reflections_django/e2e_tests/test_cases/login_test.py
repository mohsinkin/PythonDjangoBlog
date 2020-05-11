import sys
import time
import unittest

sys.path.append("/Users/mosster/PythonDjangoBlog/reflections_django/e2e_tests/")
sys.path.append("/Users/mosster/PythonDjangoBlog/reflections_django/project_env/lib/python3.8/site-packages")

from selenium import webdriver

import HtmlTestRunner
from custom_page_objects.LoginPage import LoginPage

print(sys.path)
class LoginTest(unittest.TestCase):
    base_URL = "https://moss-blog.herokuapp.com/login"
    username = "test_headless"
    password = "Testing!@"
    driver = webdriver.Chrome(
        executable_path="/Users/mosster/PythonDjangoBlog/reflections_django/e2e_tests/drivers/chromedriver",
    )

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.base_URL)
        cls.driver.maximize_window()

    def test_login(self):
        login_page_instance = LoginPage(self.driver)
        login_page_instance.set_username(self.username)
        login_page_instance.set_password(self.password)
        login_page_instance.click_login()
        self.assertEqual(
            self.driver.title, "Reflections", "Webpage Title does not match!"
        )
        login_page_instance.click_logout()
        logout_messsage = login_page_instance.get_logout_message()
        self.assertEqual(logout_messsage, "You have been logged out.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            report_title="E2E Test Results", output="../reports"
        )
    )
