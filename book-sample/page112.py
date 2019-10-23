for i in range(1, 6):
    if i == 3:
        continue
    print(i)


i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

print('###page113###')

for i in range(1, 3):
    print(i)
    for letter in ['a', 'b', 'c']:
        print(letter)
    
print('###page114###')
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

added = []
for i in list1:
    for j in list2:
        added.append(i + j)

print(added)


while input('y or n?') != 'n':
    for i in range(1, 6):
        print(i)
