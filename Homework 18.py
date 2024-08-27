class Car:
    price = 1000000
    def horse_powers(self, value):
        print(value)


class Nissan(Car):
    price = 1200000
    def horse_powers(self, value):
        print(value+24)

class Kia(Car):
    price = 150000
    def horse_powers(self, value):
        print(value+15)