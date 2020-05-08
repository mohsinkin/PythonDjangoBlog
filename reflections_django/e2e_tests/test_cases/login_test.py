import unittest
import time

import HtmlTestRunner
from selenium import webdriver
import sys

sys.path.append(
    r"C:\Users\mohsi.MOSSOSAURUSPC\PycharmProjects\PythonDjangoBlog\reflections_django\e2e_tests"
)

from page_objects.LoginPage import LoginPage


class LoginTest(unittest.TestCase):
    base_URL = "https://moss-blog.herokuapp.com/login"
    username = "test_headless"
    password = 'Testing!@'
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\mohsi.MOSSOSAURUSPC\Downloads\chromedriver.exe"
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
        self.assertEqual(
            logout_messsage.text, "You have been logged out."
        )

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            report_title="E2E Test Results", output=".\\reports"
        )
    )
