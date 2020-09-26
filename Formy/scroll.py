from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('F:\chromedriver.exe')  
driver.get('https://formy-project.herokuapp.com/scroll');

name = driver.find_element_by_id('name')

actions = ActionChains(driver)
actions.move_to_element(name)
name.send_keys('Sam Warren')

date = driver.find_element_by_id('date')
date.send_keys('01/13/1992')
# Consider adding code to fill today's date

driver.quit()
