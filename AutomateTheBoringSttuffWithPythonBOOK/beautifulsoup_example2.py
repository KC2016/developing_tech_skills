import bs4, requests

def getPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#spv-main-stage > div.xxs12of12.m5of12.l11of24.xl7of24.spv-main-info-wrapper > div.xxs12of12.spv-price-wrapper > div > span.spv-price__selling')
    return elems[0].text.strip()


price = getPrice('https://www.esprit.de/damenmode/bekleidung/t-shirts-langarmshirts/aus-leinen-mix-shirt-mit-gummizug-990EE1K310_810')   
print('The price is ' + price)
 
 