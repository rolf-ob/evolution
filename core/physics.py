def update(game):
    game.time += 1

    for plant in game.plants.copy():
        plant.age += 1
        plant.energy += 1

        if plant.age >= 100:
            game.plants.remove(plant)