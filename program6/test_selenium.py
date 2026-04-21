from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Give path of chromedriver
service = Service(r"C:\drive\chromedriver-win64\chromedriver.exe")

# Start browser
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")

# Find search box
search_box = driver.find_element(By.NAME, "q")

# Type text
search_box.send_keys("Selenium with Python")

# Press Enter
search_box.send_keys(Keys.RETURN)

# Wait
time.sleep(3)

# Close browser
driver.quit()