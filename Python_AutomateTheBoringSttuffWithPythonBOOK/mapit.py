import webbrowser
import sys
import pyperclip

# import pyperclip   # I could not install this

sys.argv  # ['mapit.py', '870', 'Valencia', 'St.']

# check if commend line arguments were passed
if len(sys.argv) > 1:
    address = ' ' .join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/870+Valencia+St,+San+Francisco,+CA+94110/')


# print(str(sys.argv))