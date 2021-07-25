import re
import pyperclip

# create a regex for phone numbers
phoneRegex = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\)))?  # area code (optional)
(\s|-)                   # first separator
\d\d\d                 # first 3 digits
-                      # separator
\d\d\d\d               # last 4 digits
(((ext(\.)?\s)|x)        # extension word-part (optional)
(\d{2,5}))?              # extension number-part (optional)
)
''', re.VERBOSE)

# create a regex for email addresses
# emailRegex = re.compile(r'[a-z0-9_.+]+ @[a-z0-9_.+]+') 
emailRegex = re.compile(r'''
# some.+_thing@(\2,5)))?.com
[a-zA-Z0-9_.+]+     # name part
@                # @ symbol
[a-zA-Z0-9_.+]+     # domain name part

''', re.VERBOSE)

# get the text off the clipboard
text = pyperclip.paste()

# get the text off the clipboard
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

print(allPhoneNumbers)
print(extractedEmail)

# copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)