import random

first = 'Мама мыла раму'
second = 'Рамена мало было'
r1 = list(map(lambda x, y: x == y, first, second))
print(r1)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        for i in data_set:
            with open(file_name, 'a') as file:
                print(str(i), file=file)
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        a = random.choice(self.words)
        return a

r3 = MysticBall('Да', 'Нет', 'Наверное', 'Зачем?')
print(r3())
print(r3())
print(r3())
