# import libraries
import json
import os.path
from urllib.request import urlopen

# Download the url
# with urlopen('https://finance.yahoo.com/webservice/vl/symbols/allcurrencies/quote?format=json') as response:
# with urlopen('http://dopaoaocaviar.com.br/category/bolo/') as response:

res = urllib.request.urlopen()
source = response.read()

#JSON
data = json.loads(source.decode('utf-8'))

import urllib.request

# https://docs.python.org/3/library/urllib.request.html#examples
# https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html
# res = urllib.request.urlopen('https://ip-ranges.amazonaws.com/ip-ranges.json')
# res_body = res.read()

# # https://docs.python.org/3/library/json.html
# j = json.loads(res_body.decode("utf-8"))

# # parse strings: 'ip_prefix' and 'region'
# #for i in range(len(j['prefixes'])):
# #	print("{0}\t{1}".format(j['prefixes'][i]['ip_prefix'], j['prefixes'][i]['region']))
# for prefix in j['prefixes']:
# 	print("{0}\t{1}".format(prefix['ip_prefix'], prefix['region']))




# print(source)
    # data = json.loads(source)
    # print(data)

'''Check if the folder files exists
directory = 'files'
parent_dir = 'COVID-19'
path = os.path.join(parent_dir, directory)  

isFile = os.path.isfile(path)  
print(isFile)'''

# create a directory if it does not exist 
directory = 'files'
if not os.path.exists(directory):
    os.makedirs(directory)

# os.makedirs(path) 
# print("Directory '%s' created" %directory) 