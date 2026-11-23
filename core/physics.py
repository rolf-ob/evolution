import random as ran

from entities.creatures import Plant, Herbivore, Carnivore
from constants import FPS, DAYNIGHT_CYCLE_SECONDS

def update_plants(game):
    for plant in game.plants.copy():
        plant.age += 1
        plant.energy += 1

        if plant.energy >= plant.lust:
            game.plants.append(Plant(
                plant.x + ran.choice([ran.randint(-40, -10), ran.randint(10, 40)]),
                plant.y + ran.choice([ran.randint(-40, -10), ran.randint(10, 40)]),
                energy=0,
                lust=max(500, plant.lust + ran.randint(-50, 50))
            ))
            plant.energy = 0

        if plant.age >= 4 * DAYNIGHT_CYCLE_SECONDS * FPS:
            game.plants.remove(plant)

def update_herbivores(game):
    for herbivore in game.herbivores.copy():
        herbivore.age += 1
        herbivore.sleep -= 1
        herbivore.food -= 1

        if herbivore.food <= 8:
            nearby_plant = None
            for plant in game.plants:
                if (
                    abs(herbivore.x - plant.x) < herbivore.sight and
                    abs(herbivore.y - plant.y) < herbivore.sight
                ):
                    nearby_plant = plant
                    break

            if nearby_plant:
                herbivore.x, herbivore.y = nearby_plant.x, nearby_plant.y
                game.plants.remove(nearby_plant)
                herbivore.food += 20
            else:
                herbivore.x += ran.randint(-20, 20)
                herbivore.y += ran.randint(-20, 20)

        elif herbivore.sleep <= 5:
            herbivore.sleep += 100
            continue

        elif herbivore.sleep >= herbivore.lust:
            nearby_mate = None
            for other_herbivore in game.herbivores.copy():
                if id(other_herbivore) != id(herbivore) and (
                    abs(herbivore.x - other_herbivore.x) < herbivore.sight and
                    abs(herbivore.y - other_herbivore.y) < herbivore.sight
                ):
                    nearby_mate = other_herbivore
                    break

            if nearby_mate:
                game.herbivores.append(Herbivore(
                    herbivore.x,
                    herbivore.y,
                    sleep=100,
                    food=40,
                    lust=max(500, herbivore.lust + ran.randint(-50, 50)),
                    sight=herbivore.sight + ran.randint(-5, 5)
                ))
                herbivore.sleep //= 4
                other_herbivore.sleep //= 4
            else:
                herbivore.x += ran.randint(-20, 20)
                herbivore.y += ran.randint(-20, 20)

        if herbivore.food <= 0 or herbivore.age > 2 * DAYNIGHT_CYCLE_SECONDS * FPS:
            game.herbivores.remove(herbivore)

def update(game):
    game.time += 1

    update_plants(game)
    update_herbivores(game)