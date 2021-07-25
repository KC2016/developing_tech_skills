import re
namesRegex = re.compile(r'Agent \w+')
names = namesRegex.findall(
    'Agent Alice gave the secret documents to Agent Bob.'
    )

names1 = namesRegex.sub(
    'REDACTED', 
    'Agent Alice gave the secret documents to Agent Bob.'
    )

print(names1)