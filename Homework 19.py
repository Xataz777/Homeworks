class Vehicle:
    vehicle_type = 'none'


class Car:
    price = 1000000
    def horse_powers(self, value):
        return value

class Nissan(Vehicle, Car):
    vehicle_type = 'car'
    price = 1300000
    def horse_powers(self, value):
        return value+15


obj = Nissan
print(obj.vehicle_type, obj.price)