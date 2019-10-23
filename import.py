import os
from datetime import datetime 
# print(os.getcwd())

print(os.getcwd())

# os.makedirs('OS-Demo-2/aaa')
# os.rmdir('OS-Demo-2/aaa')
# # os.rename('demo.txt','demo2.txt')
# print(os.stat('demo2.txt').st_mtime)
# print(datetime.fromtimestamp(os.stat('demo2.txt').st_mtime))
# print(os.listdir())

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Riles:', filenames)
    print()
