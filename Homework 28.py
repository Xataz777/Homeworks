first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

res1 = [len(x) for x in first_strings if len(x) >= 5]
res2 = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
res3 = {x:len(x) for x in first_strings + second_strings if len(x) % 2 == 0}

print(res1)
print(res2)
print(res3)