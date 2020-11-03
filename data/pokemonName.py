from bs4 import BeautifulSoup
from selenium import webdriver
# import time
import json

driver = webdriver.Chrome('chromedriver')
file = open("pokemonKor.json", "w", encoding='utf-8')
url = "https://namu.wiki/w/%ED%8F%AC%EC%BC%93%EB%AA%AC%EC%8A%A4%ED%84%B0/%EB%AA%A9%EB%A1%9D/%EC%A0%84%EA%B5%AD%EB%8F%84%EA%B0%90"
driver.get(url)
# time.sleep(5)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

dex = []

for i in range(12, 28, 2):
    gen = soup.select(
        f'#app > div > div:nth-child(2) > article > div:nth-child(5) > div:nth-child(2) > div > div > div:nth-child({i}) > div.wiki-table-wrap.table-center > table > tbody > tr')
    for mon in gen:
        name = mon.select_one('td:nth-child(3) > div').text
        numText = mon.select_one('td:nth-child(1) > div').text
        if name != " 타입 " and numText != "[B]" and numText != "[C]" and numText != "" and numText != "?":
            num = int(numText)
            # print(num, name)
            info = {'dex': num, 'speciesNameKor': name}
            dex.append(info)

file.write(json.dumps(dex, ensure_ascii=False))
file.close()
driver.quit()
