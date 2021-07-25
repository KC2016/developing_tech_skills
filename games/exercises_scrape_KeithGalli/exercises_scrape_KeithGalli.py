''' FROM THE CLASS AT https://www.youtube.com/watch?v=GjKQ6V_ViQE '''

import requests
from bs4 import BeautifulSoup as bs

# load the webpage content
r = requests.get("http://keithgalli.github.io/web-scraping/webpage.html")

# convert to a beautiful soup object
webpage = bs(r.content, "lxml")

# print out our html
# print(webpage.prettify())

# ------------ EXERCISE 1 ------------

# Grab all the social links from the webpage
# Do in 3 different ways

## 1- slicing by index, selecting the 3rd, 4th, 5th and 6th links from the webpage
social_links_1 = webpage.find_all("a")[2:6]
# print(social_links_1)

## 2- pass attributes
social_links_2 = webpage.find_all("ul", attrs={"class": "socials"})
# print(social_links_2)
## similar soluction:
# links = webpage.find("ul", attrs={"class": "socials"})  # this is a single tag element
# so...
ulist = webpage.find("ul", attrs={"class": "socials"})
links_2 = ulist.find_all("a")
actual_links_2 = [link["href"] for link in links_2]
# print(actual_links_2)


## 3- nest find/findlall
body= webpage.find("body")
ul = body.find_all('ul')[1]
# print(ul)

## 4- search for specific stings in our find/find_all calls
import re    # regex library
link_instagram = webpage.find_all("a", string = re.compile("www.instagram"))
link_twitter = webpage.find_all("a", string = re.compile("twitter"))
link_linkedin = webpage.find_all("a", string = re.compile("linkedin"))
link_tiktok = webpage.find_all("a", string = re.compile("tiktok"))

# print(link_instagram, link_twitter, link_linkedin, link_tiktok)

## 5- using select css method 
# # CSS selector reference at https://www.w3schools.com/cssref/css_selectors.asp

social_links_5a = webpage.select("body  ul  li a")[1:]
# print(social_links_5a) 

social_links_5b = webpage.select("b ~ a") # at the same level (simblings)
# print(social_links_5b) 

## Solutions:

links = webpage.select("ul.socials a")
actual_links = [link["href"] for link in links]
# print(actual_links)

links_3 = webpage.select("li.social a ")
# print(links_3)


# ------------ EXERCISE 2 ------------

## grab the table from his webpage
# the best way to scrape a table is using pandas
import pandas as pd

table = webpage.select("table.hockey-stats")[0]  
# table with a class hockey-stats; 
# [0] describe the only element and transform in a list, so I can use prettify()

columns = table.find("thead").find_all("th")
column_names = [c.string for c in columns]

table_rows = table.find("tbody").find_all("tr")
l= []
for tr in table_rows:
    td = tr.find_all('td')
    row = [str(tr.get_text()).strip() for tr in td]
    l.append(row)

df = pd.DataFrame(l, columns=column_names)
print(df.head())


# ------------ EXERCISE 3 ------------

## Grab all fun facts from his webpage
facts = webpage.select("ul.fun-facts li")
facts_with_is = [fact.find(string=re.compile("is")) for fact in facts]
# facts_with_is = [fact for fact in facts_with_is if fact] # scrape the facts that has 'is' 
## here it stop on 'is' and striping out the rest, because the text has italic marks ,<i> </i>, WRONG
facts_with_is = [fact.find_parent().get_text() for fact in facts_with_is if fact]

# print(facts_with_is)


# ------------ EXERCISE 4 ------------

## Download one of the images

## solution: (with adjustments)
base_url = "http://keithgalli.github.io/web-scraping/"
images = webpage.select("div.row div.column img")
image_url = images[0]['src']
full_url = base_url + image_url

img_data = requests.get(full_url).content
with open('exercises_scrape_KeithGalli/lake_como.jpg', 'wb') as handler:
    handler.write(img_data)

# ------------ EXERCISE 5 ------------

## Solve the mistery
files = webpage.select("div.block a ")
relative_files = [f['href'] for f in files]


for f in relative_files:
    full_url_href = base_url + f
    page = requests.get(full_url_href)
    bs_page = bs(page.content)
    secret_word_element = bs_page.find("p", attrs={"id": "secret-word"})
    secret_word = secret_word_element.string
    print(secret_word)

