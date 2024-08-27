import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
    def run(self):
        enemy = 100
        day = 0
        print(f'{self.name}, на нас напали!')
        while enemy > 0:
            enemy -= self.power
            time.sleep(1)
            day += 1
            print(f'{self.name} сражается {day} дней (день), осталось {enemy} воинов')
        print(f'{self.name} одержал победу спустя {day} дней')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
time.sleep(0.05)
second_knight.start()