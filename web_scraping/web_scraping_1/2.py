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

def average_yield(country):
    yield_sum = 0
    yield_count = 0
    for idx in range(len(Country)):
        if Country[idx] == country:
            yield_sum += Yield[idx]
            yield_count += 1
    return yield_sum / yield_count

for country in set(Country[1:]):
    print(country, ': средняя мощность взрыва', average_yield(country), 'мегатон')

for i in range(len(Country)):
    if Country[i]=='USA':
        yield_USA = average_yield(Country[i])
    if Country[i]=='Soviet Union':
        yield_Soviet_Union = average_yield(Country[i])

if yield_USA > yield_Soviet_Union:
    print('USA')
else:
    print('Soviet Union')


