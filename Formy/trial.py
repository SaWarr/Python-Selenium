import time
from selenium import webdriver

driver = webdriver.Chrome('F:\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://formy-project.herokuapp.com/');

logo = driver.find_element_by_id("logo")
print(logo.text)
driver.quit()