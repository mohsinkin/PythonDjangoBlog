import unittest
from selenium import webdriver

class CreatePostTest(unittest.TestCase):
    def test_load_composer(self):
        self.driver = webdriver.Chrome(
            executable_path=r"C:\Users\mohsi.MOSSOSAURUSPC\Downloads\chromedriver.exe"
        )
        self.driver.get("https://moss-blog.herokuapp.com/")
        print('Title of the page is: ', self.driver.title)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()