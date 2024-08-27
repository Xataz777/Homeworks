class Building:
    def __init__(self, floors, type):
        self.numberOfFloors = floors
        self.buildingType = type
    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors, self.buildingType == other.buildingType


h1 = Building(5, 'Пятиэтажка')
h2 = Building(9, 'Девятиэтажка')
print(h1 == h2)