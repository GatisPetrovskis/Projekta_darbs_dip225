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
time.sleep(5)