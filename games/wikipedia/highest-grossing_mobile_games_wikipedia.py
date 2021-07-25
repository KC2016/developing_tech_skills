# ios top app charts

import bs4 as bs
import urllib.request
import pandas as pd
import csv

# reader/writer variables
url = 'https://en.wikipedia.org/wiki/List_of_highest-grossing_mobile_games'
csv_file_name = 'highest-grossing_mobile_games_wikipedia.csv'

# URL reader
sauce = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(sauce, 'lxml')

# CSV writer
wtr = csv.writer(open(csv_file_name, 'w'), delimiter=',', lineterminator='\n')


# ------ START SCRAPE ALGORITHM ------

table = soup.find('table')  
rows = table.find_all('tr')

# get headers
headers = [v.text for v in rows[0].find_all('th')]
wtr.writerow(headers)

# get data rows
for i in range(1, len(rows)):
    dataRow = [v.text for v in rows[i].find_all('td')]
    wtr.writerow(dataRow)

# ------ END SCRAPE ALGORITHM ------