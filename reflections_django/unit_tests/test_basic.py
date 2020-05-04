import unittest
from selenium import webdriver

class CreatePostTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r"C:\Users\mohsi.MOSSOSAURUSPC\Downloads\chromedriver.exe"
        )
        self.driver.get("https://moss-blog.herokuapp.com/")

    def test_title(self):
        blog_title = self.driver.title
        self.assertEqual(blog_title, 'Reflections')

    def test_blog_name(self):
        blog_name = self.driver.find_element_by_xpath('/html/body/header/nav/div/a')
        self.assertEqual(blog_name.text, 'Reflections Blog')

    def tearDown(self):
        self.driver.close
        self.driver.quit

if __name__ == '__main__':
    unittest.main(exit=False)