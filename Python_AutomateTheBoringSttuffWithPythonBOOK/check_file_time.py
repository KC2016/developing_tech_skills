import urllib.request
import os.path
import zipfile
import pathlib
import json
from datetime import date
import time

print('COVID-19: a summary of new and total cases per country updated daily.')

# Create a directory if it does not exist 
filesDir = 'files'
if not os.path.exists(filesDir):
    os.makedirs(filesDir)

# Defines functions and classes which help in opening URLs (mostly HTTP) in a complex world
# Retrieves the contents of url and places it in filename.
endPointUrl = 'https://api.covid19api.com/summary'
jsonFileName = 'summary.json'
zipFileName = 'summary.zip'

# Create the relative path of the zip file
relativeZipFilePath = os.path.join(filesDir, zipFileName)
         
# stat = os.stat(relativeZipFilePath)       
# print(stat.st_birthtime)

# stat.st_mtime   # last modification

print("last modified: %s" % time.ctime(os.path.getmtime(relativeZipFilePath)))
print("created: %s" % time.ctime(os.path.getctime(relativeZipFilePath)))