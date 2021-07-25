import re
consonantsRegex = re.compile(r'[^aeiouAEIOU]')
cons = consonantsRegex.findall('Robocop eats baby food.')
print(cons)

print(
    '''findall() returns all matches; 
if regex has 0 or 1 group, findall() returns a list of strings;
of it has 2 or nore groups, findall() returns a list of tuples of strings;
\d is a shorthand character class that match digits;
\w matches words characters;
\s matches white spaces;
uppercase \D,\W,\S match characteres that are NOT digits, word characters and spaces;
^caret makes it a negative character class;
I can make my own character classes with square brackets: [aeiou];
'''
)