import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('F:\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://formy-project.herokuapp.com/autocomplete');

autocomplete = driver.find_element_by_id('autocomplete')
autocomplete.send_keys('42 wallaby way, new beith qld, australia')


autocompleteResult = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CLASS_NAME, 'pac-item'))
	)

# autocompleteResult = driver.find_element_by_class_name('pac-item')
autocompleteResult.click()

driver.quit()