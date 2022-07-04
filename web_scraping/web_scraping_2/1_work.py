import requests
from bs4 import BeautifulSoup

website_url = requests.get('https://en.wikipedia.org/wiki/List_of_Rick_and_Morty_episodes').text
soup = BeautifulSoup(website_url,'lxml')
My_table = soup.find_all('table',{'class':'wikitable plainrowheaders wikiepisodetable'})
rows = My_table[0].find_all('tr')

titles = []
directors = []
viewers = []

titles.append(rows[0].find_all('th')[2].get_text().strip())
directors.append(rows[0].find_all('th')[3].get_text().strip())
viewers.append(rows[0].find_all('th')[6].get_text().strip())

for row in rows[1:]:
    r = row.find_all('td')
    titles.append(r[1].get_text().strip())

for row in rows[1:]:
    r = row.find_all('td')
    directors.append(r[2].get_text().strip())

for row in rows[1:]:
    r = row.find_all('td')
    viewers.append(r[5].get_text().strip())
    
print(titles)
print(directors)
print(viewers)
