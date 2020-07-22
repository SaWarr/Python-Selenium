# Python Selenium work
# 20200722 - Page navigation work

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("fakeblogwebsite.tech")

link = driver.find_element_by_link_text("Blog")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK-TEXT, "July Posts"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK-TEXT, "July 18th"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "thumb-button"))
    )
    element.click()

    performance = driver.find_element_by_ID("thumb-count")
    print(performance.text)

    driver.back()
    driver.back()
    driver.back()

except:
    driver.quit()
