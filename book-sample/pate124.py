import os

print(os.path.join('user','bob','st.txt'))

# st = open('st.txt','w')
# st.write('Hi from python!')
# st.close()

# st = open('st2.txt','w')
# st.write('pythonから日本語')
# st.close()

st = open('st.txt','w', encoding='utf-8')
st.write('pythonから日本語')
st.close()

st = open('st.txt','r', encoding='utf-8')
print(st.read())
st.close()