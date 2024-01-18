from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime
import time
service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)

datums = datetime.datetime.now()
diena = datums.day
menesis = datums.month

url = f"https://www.rtu.lv/lv/sports/sporta-nodarbibas/pieteikties-nodarbibam?sport_type_id=&sport_lesson_id=&sport_trainer_id=&sport_address_id=&gender=&master_type=0&calendar_date=2024-0{menesis}-{diena}&calendar_view=agendaWeek#d=2024-0{menesis}-{diena}&v=agendaWeek"
driver.get(url)
time.sleep(3)
sikfaili = driver.find_element(By.XPATH, '/html/body/div[16]/div/div/div/div/div[2]/a[1]')
sikfaili.click()
time.sleep(1)

linki = []
find = driver.find_elements(By.TAG_NAME, "a")
for x in find:
    value = x.get_attribute("innerText")
    if "Volejbols" in value:
        linki.append(x.get_attribute("href"))

for elem in linki:
    driver.get(elem)
    time.sleep(3)
    adrese = driver.find_element(By.XPATH, "/html/body/div[14]/div/div/div[2]/div[1]/div/table/tbody/tr[5]/td/a").get_attribute("innerText")
    print(adrese)