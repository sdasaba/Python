# fruits = ['apple', 'orange', 'tomato']
# print(fruits)
# print(len(fruits))

# fruits = ('Apple', 'Orange', 'Grapes')
# fruits2 = tuple(('Apple', 'Orange', 'Grapes'))

# person = {
#     'first_name': 'John',
#     'last_name': 'Doe',
#     'age': 30
# }

# person2 = dict(first_name='Sara',)

# print(person)
# print(person['first_name'])

# person['phone'] = '555-5555-5555'
# print(person)
# print(person.keys())
# print(person.items())

# def sayHello(name):
#     print(f'Hello {name}')

# sayHello('Lee wangi')

# x = 10
# y = 50

# if x > y:
#     print(f'{x} is greater than {y}')
# else:
#     print(f'{y} is greater than {x}')

# people = ['lee','ok','choi','seo']

# for person in people:
#     print(f'Current person: {person}')

# for i in range(0, 11):
#     print(f'Number: {i}')

# core modules 
import datetime
from datetime import date
import time
from time import time

# pip module
from camelcase import CamelCase

# today = datetime.date.today()
today = date.today()
timestamp = time()

c = CamelCase()

print(c.hump('Hello there world'))

print(timestamp)