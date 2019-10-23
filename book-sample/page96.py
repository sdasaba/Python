equ = 'All animals are equal.'
equ = equ.replace('a','@')

print(equ)

print('animals'.index('m'))
try:
    print('animals'.index('z'))
except:
    print('찾지못하였습니다.')