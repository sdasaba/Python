myFile = open('myFile.txt', 'w')

print('name: ', myFile.name)
print('Is Close: ', myFile.closed)
print('opening Mode: ', myFile.mode)


myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()


myFile = open('myfile.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()

myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)