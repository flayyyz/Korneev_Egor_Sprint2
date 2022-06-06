# -*- coding: utf-8 -*-
file = input('Укажите файл: ')
with open(file, 'rb') as f:
  data = f.read(2)
'''
print(data.decode('utf-8'))
'''
string = data.decode('utf-8')
if "MZ" in string:
  print("executable, OS Windows ")
else:
  print("non-executable")