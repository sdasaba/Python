author = 'kafka'

try:
    print(author[0])
    print(author[1])
    print(author[2])
    print(author[3])
    # print(author[4])
    # print(author[5])
except IndexError:
    print('범위를 벗어났습니다')
