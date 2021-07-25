import re

phoneRegex = re.compile(r'\d\d\d\d \d\d\d\d \d\d\d\d')
resume = '''Karina 
Data Analyst

country
github

phone
contacts

Email


Skills

Wprks

Achievements


'''

tel = phoneRegex.findall(resume)
print(tel)