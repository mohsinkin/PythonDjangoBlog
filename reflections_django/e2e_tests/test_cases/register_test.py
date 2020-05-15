import sys
import time
import unittest

sys.path.append("/Users/mosster/PythonDjangoBlog/reflections_django/e2e_tests/")
sys.path.append("/Users/mosster/PythonDjangoBlog/reflections_django/project_env/lib/python3.8/site-packages")

from selenium import webdriver

import HtmlTestRunner
from custom_page_objects.RegisterPage import RegisterPage



class RegisterTest(unittest.TestCase):
    base_URL = "https://moss-blog.herokuapp.com/register"
    username = "test_register"
    password = "Testing!@"
    email = "register@example.com"
    driver = webdriver.Chrome(
        executable_path="/Users/mosster/PythonDjangoBlog/reflections_django/e2e_tests/drivers/chromedriver",
    )

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.base_URL)
        cls.driver.maximize_window()

    def test_register(self):
        register_page_instance = RegisterPage(self.driver)
        register_page_instance.set_username(self.username)
        register_page_instance.set_email(self.email)
        register_page_instance.set_password(self.password)
        register_page_instance.set_password_confirmation(self.password)

        register_page_instance.click_signup()
        register_message = register_page_instance.get_register_message()

        self.assertEqual(
            self.driver.title, "Reflections", "Webpage Title does not match!"
        )
        self.assertEqual(
            register_message,
            f"Account created for {self.username}! You are now able to login.",
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
