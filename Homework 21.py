text = 'Text_1.txt'
with open(text, mode='r', encoding='utf-8') as file:
    for line in file:
        print(line, end='')