#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import csv

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

data = []
scrapesite = '' # Enter url to scrape

if __name__ == '__main__':
    print("Scraper started")
    page = requests.get(scapesite, headers=headers)
    soup = BeautifulSoup(page.text, 'html5lib')
    table = soup.find('table', attrs={'class':'dataTable'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols]) # Get rid of empty values
    print(data)

    with open('output.csv', 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for x in data:
            wr.writerow(x)