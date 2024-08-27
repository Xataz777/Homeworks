class House:
    def __init__(self, name, floor):
        self.name = name
        self.floor = floor
    def go_to(self, new_floor):
        if self.floor > new_floor:
            for a in range(1, new_floor):
                print(a)
        else:
            print('Такого этажа не существует')


h1 = House('ЖК Свечка', 15)
h2 = House('Хрущёвка', 5)
h1.go_to(4)
h2.go_to(7)