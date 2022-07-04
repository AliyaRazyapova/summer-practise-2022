import requests

website_url = requests.get('https://en.wikipedia.org/wiki/List_of_nuclear_weapons_tests').text

from bs4 import BeautifulSoup

soup = BeautifulSoup(website_url,'lxml')

My_table = soup.find_all('table',{'class':'wikitable sortable'})
rows = My_table[1].find_all('tr')

Dates = []
Dates.append(rows[0].find_all('th')[0].get_text().strip())

for row in rows[1:]:
    r = row.find_all('td')
    Dates.append(r[0].get_text().strip())

Yield = []
Yield.append(rows[0].find_all('th')[1].get_text().strip())

for row in rows[1:]:
    r = row.find_all('td')
    Yield.append(float(r[1].get_text().strip()))

Country = []
Country.append(rows[0].find_all('th')[3].get_text().strip())

for row in rows[1:]:
    r = row.find_all('td')
    Country.append(r[3].get_text().strip())

print(Dates)
print(Yield)
print(Country)
