first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

a = zip(first, second)
res1 = (len(i[0]) - len(i[1]) for i in a if len(i[0]) != len(i[1]))

b = []
for i in range(len(first)):
    b.append((first[i], second[i]))

res2 = (False if len(i[0]) != len(i[1]) else True for i in b)

print(list(res1))
print(list(res2))