# ios top app charts

import bs4 as bs
import urllib.request
import pandas as pd
import csv

# reader/writer variables
url = 'https://www.appannie.com/apps/ios/top-chart?country=US&category=36&device=iphone&date=2020-12-26&feed=All&page_number=0&page_size=100&rank_sorting_type=rank'
csv_file_name = 'ios_top_app_charts.csv'

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