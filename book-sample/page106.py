people = {
    'aaa':'AAA',
    'bbb':'BBB',
    'ccc':'CCC'
}

for character in people:
    print(character)


tv = ['aaaa','bbbb','cccc']

for i ,new in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i]=new

print(tv)