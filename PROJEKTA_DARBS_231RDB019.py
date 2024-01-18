from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import datetime
import time
import pandas as pd
service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)

datums = datetime.datetime.now()
diena = datums.day
menesis = datums.month
saite = f"https://www.rtu.lv/lv/sports/sporta-nodarbibas/pieteikties-nodarbibam?sport_type_id=&sport_lesson_id=&sport_trainer_id=&sport_address_id=&gender=&master_type=0&calendar_date=2024-0{menesis}-{diena}&calendar_view=agendaWeek#d=2024-0{menesis}-{diena}&v=agendaWeek"

def lietotaja_ievade():
    while True:
        ievade = input("Ievadiet sporta nodarbību Piemēram - Volejbols, Basketbols, Joga , Peldēšana")
        if (not ievade):
            print("Ievadiet vertību vēlreiz: ")
        else:
            break 
    return ievade
sports = lietotaja_ievade()

def saites(sports, url):
    driver.get(url)
    time.sleep(3)
    try:
        sikfaili = driver.find_element(By.CLASS_NAME, "uce-disable")
        sikfaili.click()
        poga = driver.find_element(By.XPATH, '//*[@id="unibit_modal_popup"]/div/div/div/div/div[1]')
        poga.click()
        time.sleep(1)
    except NoSuchElementException:
        pass

    linki = []
    find = driver.find_elements(By.TAG_NAME, "a")
    for x in find:
        value = x.get_attribute("innerText")
        if f"{sports}" in value and "RTU darbiniekiem" not in value:
            linki.append(x.get_attribute("href"))

    nakama_nedela = driver.find_elements(By.TAG_NAME, "button")
    for nakama in nakama_nedela:
        if  "fc-next-button" in nakama.get_attribute("class"):
            nakama.click()
            break
    time.sleep(1)

    find_2 = driver.find_elements(By.TAG_NAME, "a")
    for x in find_2:
        value = x.get_attribute("innerText")
        if f"{sports}" in value and "RTU darbiniekiem" not in value:
            linki.append(x.get_attribute("href"))
    return linki

def iegust_tabulas(linki):
    tabulas = []
    for elem in linki:
        driver.get(elem)
        time.sleep(1)
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
    return tabulas

def excel_datne(tabulas, sports):
    if len(tabulas) > 0:
        df = pd.concat(tabulas, ignore_index=True)
        df.index = df.index + 1
        if 'Dalībnieku skaits' in df.columns and df["Dalībnieku skaits"].isnull().values.any() == False:
            df['Dalībnieku skaits'] = df['Dalībnieku skaits'].astype('int')
        if 'Maksimālais dalībnieku skaits' in df.columns and df["Maksimālais dalībnieku skaits"].isnull().values.any() == False:
            df['Maksimālais dalībnieku skaits'] = df['Maksimālais dalībnieku skaits'].astype('int')
        if 'Minimālais dalībnieku skaits' in df.columns and df["Minimālais dalībnieku skaits"].isnull().values.any() == False:
            df['Minimālais dalībnieku skaits'] = df['Minimālais dalībnieku skaits'].astype('int')
        df.to_excel(f"{sports}.xlsx")
    else:
        print("Nevarēja atrast atbilstošus notikumus ievadītajam, mēģiniet vēlreiz")
majaslapas = saites(sports, saite)
tabulas = iegust_tabulas(majaslapas)
excel_datne(tabulas, sports)