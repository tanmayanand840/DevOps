import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        service = Service(r"C:\drive\chromedriver-win64\chromedriver.exe")
        self.browser = webdriver.Chrome(service=service)

    def tearDown(self):
        self.browser.quit()

    def test_page_title(self):
        self.browser.get("https://www.google.com")
        self.assertIn("Google", self.browser.title)

if __name__ == "__main__":
    unittest.main()