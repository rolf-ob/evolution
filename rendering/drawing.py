import pygame as py
import math

from core.spatial import world_to_screen
from constants import FPS

def draw(game):
    screen = game.screen
    light = 127.5 * (1 - math.cos(2 * math.pi * 0.05 * (game.time / FPS)))
    screen.fill((0, 0, light))

    for plant in game.plants:
        x, y = world_to_screen(game, plant.x, plant.y)
        py.draw.circle(screen, (0, 255, 0), (x, y), 10)

    for plant in game.herbivores:
        x, y = world_to_screen(game, plant.x, plant.y)
        py.draw.circle(screen, (255, 255, 0), (x, y), 10)

    for plant in game.carnivores:
        x, y = world_to_screen(game, plant.x, plant.y)
        py.draw.circle(screen, (255, 0, 0), (x, y), 10)