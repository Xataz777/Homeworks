class House:
    def __init__(self):
        self.numberOfFloors = 0
    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print('Новое кол-во этажей в доме:',self.numberOfFloors)


h1 = House()
h1.setNewNumberOfFloors(4)