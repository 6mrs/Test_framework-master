import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://10.0.1.183/youjia-admin/login"
base_path = os.path.dirname(os.path.abspath(__file__)) + '/../..'
driver_path = os.path.abspath(base_path+'/drivers/chromedriver')

locator_kw = (By.ID, 'kw')
locator_su = (By.ID, 'su')
locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

driver = webdriver.Chrome(executable_path=driver_path)
driver.get(URL)
driver.find_element(*locator_kw).send_keys('selenium')
driver.find_element(*locator_su).click()
time.sleep(2)
links = driver.find_elements(*locator_result)
for link in links:
    print(link.text)
time.sleep(3)
driver.quit()