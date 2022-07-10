import requests
from bs4 import BeautifulSoup
import bs4

import httplib2 
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import gSheetsDataExtractor

spreadsheet_id = '1cV5r6saSpKsiUG_Vtnc2Nl1Vx4VWz5HWsJy3XB_2zxg'
# Читаем ключи из файла
credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json',
                                                               ['https://www.googleapis.com/auth/spreadsheets',
                                                                'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

from fake_useragent import UserAgent
ua = UserAgent()
headers = {'User-Agent': ua.random}
url = 'https://vkusvill.ru/goods/gotovaya-eda/?PAGEN_1='
resp = requests.get(url, headers=headers).text
soup = bs4.BeautifulSoup(resp, 'lxml')

list_of_urls = []
for i in range (4,38):
    list_of_urls.append(url + str(i))
print(list_of_urls)

products_name = []
products_coast = []
categorya = []

for chapter_url in list_of_urls:
    chapter = bs4.BeautifulSoup(requests.get(chapter_url).text, 'lxml').find_all('div', class_='Slider__itemInner')
    #print(chapter[0])
    for product in chapter:

        ab = product.find("a", class_="ProductCard__link js-datalayer-catalog-list-name")
        #print(ab)
        #stop
        if ab is None:
            break
        else:
            products_name.append(ab.text.strip())
                
        ac = product.find("span", class_="Price__value")
        if ac is None:
            break
        else:
            products_coast.append(ac.text.strip().split()[0])
        #print(ac.text.strip().split()[0])

        ad = soup.find('span', class_='VVCatalog2020Menu__LinkCol _text')
        #print(ad.text.strip())
        categorya.append(ad.text.strip())

print(len(products_coast), len(products_name), len(categorya))
values = service.spreadsheets().values().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": f"A791:C{791+len(products_name)}",
             "majorDimension": "COLUMNS",
             "values": [categorya, products_name, products_coast]}
        ]
    }
).execute()

