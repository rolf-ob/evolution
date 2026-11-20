class Plant:
    def __init__(self, x, y, energy, age=0):
        self.x = x
        self.y = y
        self.age = age
        self.energy = energy

class Herbivore:
    def __init__(self, x, y, energy, hunger, lust, age=0):
        self.x = x
        self.y = y
        self.age = age
        self.energy = energy
        self.hunger = hunger
        self.lust = lust

class Carnivore:
    def __init__(self, x, y, energy, hunger, lust, age=0):
        self.x = x
        self.y = y
        self.age = age
        self.energy = energy
        self.hunger = hunger
        self.lust = lust