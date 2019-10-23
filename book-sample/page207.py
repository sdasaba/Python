import re

l = 'Beautiful is better than ugly.'
matches = re.findall('Beautiful', l)

print(matches)

matches2 = re.findall('beautiful', l, re.IGNORECASE)
print(matches2)