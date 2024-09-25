import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://microsoft.com")
print(driver.current_url)
print(driver.title)
time.sleep(3)