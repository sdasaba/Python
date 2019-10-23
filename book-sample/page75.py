colors = ['blue','green','yello']

print('black' is not colors)

print(len(colors))

guess = input('무슨 색 입니까? =>')

if guess in colors:
    print('정답입니다')
else:
    print('틀렸습니다.아쉬워요')
