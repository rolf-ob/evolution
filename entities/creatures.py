class Plant:
    def __init__(self, x, y, energy, lust, age=0):
        self.x = x
        self.y = y
        self.energy = energy
        self.lust = lust
        self.age = age

class Herbivore:
    def __init__(self, x, y, sleep, food, lust, sight, age=0):
        self.x = x
        self.y = y
        self.sleep = sleep
        self.food = food
        self.lust = lust
        self.sight = sight
        self.age = age

class Carnivore:
    def __init__(self, x, y, sleep, food, lust, sight, age=0):
        self.x = x
        self.y = y
        self.sleep = sleep
        self.food = food
        self.lust = lust
        self.sight = sight
        self.age = age