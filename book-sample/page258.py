# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found

number_list = range(0, 100)
s1 = ss(number_list, 2)
print(s1)

s2 = ss(number_list, 202)
print(s2)