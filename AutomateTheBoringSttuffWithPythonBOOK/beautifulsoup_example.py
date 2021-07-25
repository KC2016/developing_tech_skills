import bs4
import requests
# res = requests.get('http://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/')
res = requests.get('https://www.who.int/emergencies/diseases/novel-coronavirus-2019/question-and-answers-hub/q-a-detail/q-a-coronaviruses')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# soup.select('#a-autoid-5-announce > span.a-color-secondary > span')
# elems = soup.select("#a-autoid-5-announce > span.a-color-secondary > span")

print(soup.select('#sf-accordion > div:nth-child(1) > div.sf-accordion__trigger-panel > a'))
elems = soup.select('#sf-accordion > div:nth-child(1) > div.sf-accordion__trigger-panel > a')
print(elems)
print(elems[0].text)
print(elems[0].text.strip())   # strip() returns a copy of the string 
# by removing both the leading and the trailing characters (based on the string argument passed)

