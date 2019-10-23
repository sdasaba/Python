# books = {'Dracula':'Stroker',
# '1984':'Orwell',
# 'The trial':'Kafka'}

# print(books)

# del books['The trial']
# print(books)
# books


songs = {'1':'fun',
'2':'blue',
'3':'me',
'4':'floor',
'5':'live'
}

n = input('번호를 입력해주세요:')

if n in songs:
    song = songs[n]
    print(song)
else:
    print('찾지 못하였습니다')