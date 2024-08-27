from pprint import pprint

abc = 'Text_1.txt'
file = open(abc, mode='r', encoding='utf-8')
f_read = file.read()
file.close()
pprint(f_read)
