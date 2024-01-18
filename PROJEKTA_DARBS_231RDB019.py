from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime
import time
import pandas as pd
service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)

datums = datetime.datetime.now()
diena = datums.day
menesis = datums.month

url = f"https://www.rtu.lv/lv/sports/sporta-nodarbibas/pieteikties-nodarbibam?sport_type_id=&sport_lesson_id=&sport_trainer_id=&sport_address_id=&gender=&master_type=0&calendar_date=2024-0{menesis}-{diena}&calendar_view=agendaWeek#d=2024-0{menesis}-{diena}&v=agendaWeek"
driver.get(url)
time.sleep(3)
sikfaili = driver.find_element(By.CLASS_NAME, "uce-disable")
sikfaili.click()
poga = driver.find_element(By.XPATH, '//*[@id="unibit_modal_popup"]/div/div/div/div/div[1]')
poga.click()
time.sleep(1)

linki = []
find = driver.find_elements(By.TAG_NAME, "a")
for x in find:
    value = x.get_attribute("innerText")
    if "Volejbols" in value and "RTU darbiniekiem" not in value:
        linki.append(x.get_attribute("href"))
tabulas = []
for elem in linki:
    driver.get(elem)
    time.sleep(2)
    final = []
    tabula = driver.find_element(By.TAG_NAME, "tbody").get_attribute("innerText")
    splited = tabula.rstrip().replace("\t", "").split("\n")
    for x in splited:
        vertiba = x.split(":", 1)
        for y in vertiba:
            final.append(y)

    vardnica = {}
    for i in range(0, len(final), 2):
        vardnica[final[i]] = [final[i + 1]]
    if int(vardnica.get("Laiks")[0][0:2]) >= diena and "Atcelts" not in vardnica:
        jauns = pd.DataFrame.from_dict(vardnica)
        tabulas.append(jauns)

df = pd.concat(tabulas, ignore_index=True)
df.index = df.index + 1
df.to_excel("Volejbols.xlsx")
print(df)