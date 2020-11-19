from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json

driver = webdriver.Chrome('chromedriver')
file = open("moveKor.json", "w", encoding='utf-8')
url = "https://pokemon.fandom.com/ko/wiki/%EA%B5%AD%EA%B0%80%EB%B3%84_%EA%B8%B0%EC%88%A0_%EC%9D%B4%EB%A6%84_%EB%AA%A9%EB%A1%9D"
driver.get(url)
req = driver.page_source
time.sleep(1)
soup = BeautifulSoup(req, 'html.parser')

dex = []
movelist = soup.select('#mw-content-text > div > table.prettytable.sortable.jquery-tablesorter > tbody > tr')
for move in movelist:
    nameKor = move.select_one('td:nth-child(2) > a').text.strip()
    nameEng = move.select_one('td:nth-child(4)').text.strip()
    print(nameKor, nameEng)
    info = {'name': nameEng, 'nameKor': nameKor}
    dex.append(info)

file.write(json.dumps(dex, ensure_ascii=False))
file.close()
driver.quit()