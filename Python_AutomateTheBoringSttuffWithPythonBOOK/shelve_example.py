# the file cannot be named shelve.py
import os
import shelve
from pathlib import Path

# shelfFile = shelve.open('mydata')
# shelfFile ['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-Tail', 'Cleo']
# shelfFile.close()

# shelfFile = shelve.open('mydata')
# print(shelfFile ['cats'])
# shelfFile.close()

# shelfFile = shelve.open('mydata')
# print(shelfFile.keys())
# print(list(shelfFile.keys()))
# print(list(shelfFile.values()))
# print(shelfFile.readlines())
# shelfFile.close()
import os.path
file_path = '/Tutorials/'
file_name = 'sonnet29.txt'
# os.chdir(path)
# retval = os.getcwd()
# print("Current working directory %s" % retval)

RelativePath_sonnet29 = os.path.join(file_path, file_name)
sonnetFile = open(RelativePath_sonnet29)
ReadSonnet29 = sonnetFile.readlines()
print(ReadSonnet29)


