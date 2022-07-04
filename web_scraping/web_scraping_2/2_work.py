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
print(titles)

for row in rows[1:]:
    r = row.find_all('td')
    directors.append(r[2].get_text().strip())
print(directors)

for row in rows[1:]:
    r = row.find_all('td')
    viewers.append(r[5].get_text().strip())
    
for i in range(1,len(viewers)):
    kek_1 = viewers[i]
    for j in range(len(kek_1)):
        kek_2 = kek_1[j]
        if kek_2=='[':
            number = j
            viewers[i]=float(kek_1[:number])
print(viewers)
            
season1 = {}
for i in range(1,len(titles)):
    season1[titles[i]]=[directors[i], viewers[i],i]
print(season1)

def Name(titles):
    return str(i) + " Episode " + str(titles[i]) + " directed by " + str(directors[i]) + " was watched by " + str(viewers[i]) + " million viewers in the US."
for i in range(1,len(titles)):
    print(Name(titles))

kol_vo=0
for i in range(len(titles)):
    if directors[i]=='Stephen Sandoval':
        kol_vo += viewers[i]
print(kol_vo)
