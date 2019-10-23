import glob
import csv
from pathlib import Path


print('Use glob')
print(glob.glob('.\\*'))

print('Use Path')
p = Path('.\\')

print(list(p.glob('*.py')))

print('csv output start')
f = open('output.csv', 'w')
writer = csv.writer(f, lineterminator='\n')
writer.writerow(list(p.glob('*.py')))
f.close
print('csv output finish')
