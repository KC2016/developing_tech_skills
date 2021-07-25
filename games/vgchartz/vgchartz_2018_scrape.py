import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import pprint # prettify

# reader/writer variables
url = 'https://www.vgchartz.com/games/games.php?name=&keyword=&console=&region=All&developer=&publisher=&goty_year=2018&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=200&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&showvgchartzscore=1&shownasales=0&shownasales=1&showdeveloper=0&showdeveloper=1&showcriticscore=0&showcriticscore=1&showpalsales=0&showpalsales=1&showreleasedate=0&showreleasedate=1&showuserscore=0&showuserscore=1&showjapansales=0&showjapansales=1&showlastupdate=0&showlastupdate=1&showothersales=0&showothersales=1&showshipped=0&showshipped=1'
csv_file_name = 'vgchartz/games_2018.csv'

# load the webpage content
r = requests.get(url)

# convert to a beautiful soup object
webpage = bs(r.content, "lxml")

table = webpage.select("table")[0]
# # [0] describe the only element and transform in a list, so I can use prettify()

print(table.prettify())

columns = table.find("thead").find_all("th")
# column_names = [c.string for c in columns]

# table_rows = table.find("tbody").find_all("tr")


# l= []
# for tr in table_rows:
#     td = tr.find_all('td')
#     row = [str(tr.get_text()).strip() for tr in td]
#     l.append(row)

# df = pd.DataFrame(l, columns=column_names)
# print(df.head())



# # CSV writer
# wtr = csv.writer(open(csv_file_name, 'w'), delimiter=',', lineterminator='\n')


