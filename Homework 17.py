class Building:
    total = 0
    def __init__(self, name):
        self.name = name
        Building.total += 1


obj = []
for a in range (40):
    obj.append(Building(a))
    print(Building.total)
print(obj)