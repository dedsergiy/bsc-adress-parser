import requests
import csv
import fake_useragent
from bs4 import BeautifulSoup
import time
import random

ua = fake_useragent.UserAgent()
count = int(input("How many pages do you want to analyze: "))
headers = {
    'user-agent': ua.random,
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/\
    *;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
adresses = set()
for i in range(0, count+1):
    url = 'https://bscscan.com/txs?p=' + str(i)
    r = requests.get(url, headers=headers)
    with open('bscscan.com'+str(i)+'.html', 'w', encoding='utf-8')as file:
        file.write(r.text)
    with open('bscscan.com'+str(i)+'.html', encoding='utf-8')as file:
        soup = BeautifulSoup(file, 'lxml')
        trs = soup.find('table', class_="table table-hover").find('tbody').find_all('tr')
        atters = {
            'class':'hash-tag text-truncate',
            'data-boundary':'viewport',
            'data-html':'true'
        }
        for tr in trs:
            adres = tr.find_all('span', attrs=atters)
            for a in adres:
                k = a.find('a').get('href')
                adresses.add(k.split('/')[-1])
    if count-i != 0:
        print(f'\n Scrapping {i} page BscScan complete \n'
              f'{count - i} page left to success')
    elif count-i == 0:
        print(f'\n Scrapping is complete! \n'
              f'We are scrape {count} pages \n'
              f'Check page.csv for using this data')
    time.sleep(random.randrange(2, 4))

with open('page.csv', 'w', encoding='utf-8')as tab:
    writer = csv.writer(tab)
    for adres in adresses:
        writer.writerow(adres.split())



