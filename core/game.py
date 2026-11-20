import pygame as py

from core.input import handle_input
from core.physics import update
from rendering.drawing import draw
from entities.frame_limiter import FrameLimiter
from entities.camera import Camera
from entities.creatures import Plant, Herbivore, Carnivore
from constants import WIDTH, HEIGHT, FPS

class Game:
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode((WIDTH, HEIGHT), py.RESIZABLE)
        self.frame_limiter = FrameLimiter()
        self.camera = Camera()

        self.width = WIDTH
        self.height = HEIGHT

        self.time = 0

        self.plants = [Plant(100, 0, 0)]
        self.herbivores = [Herbivore(0, 0, 5, 5, 5)]
        self.carnivores = [Carnivore(-100, 0, 5, 5, 5)]

        self.running = True

    def run(self):
        while self.running:
            handle_input(self)
            update(self)
            draw(self)
            py.display.flip()

            self.frame_limiter.limit_fps(FPS)
            self.frame_limiter.tick()

        py.quit()