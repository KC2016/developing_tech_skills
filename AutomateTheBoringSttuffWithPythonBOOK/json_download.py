import urllib.request

# Defines functions and classes which help in opening URLs (mostly HTTP) in a complex world
# Retrieves the contents of url and places it in filename.
url = 'https://api.covid19api.com/summary'
urllib.request.urlretrieve(url, 'summary.json')