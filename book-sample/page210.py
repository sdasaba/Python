import re

string = 'Two too.'
m = re.findall('t[ow]o', string, re.IGNORECASE)
print(m)

m2 = re.findall('t[w]o', string, re.IGNORECASE)
print(m2)

line = "123 hi 34 hello."
m3 = re.findall('[.0-9]', line, re.IGNORECASE)
print(m3)