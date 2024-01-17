from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome()


rinda = []
        
    
url = "https://emn178.github.io/online-tools/crc32.html"
driver.get(url)
time.sleep(2)

find = driver.find_element(By.XPATH, '//*[@id="input"]')
find.click()

find_value = driver.find_element(By.XPATH, '//*[@id="output"]')
value = find_value.get_attribute("value")