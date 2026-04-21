from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(r"C:\drive\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

assert "Google" in driver.title

time.sleep(3)
driver.quit()