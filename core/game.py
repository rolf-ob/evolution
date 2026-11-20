import pygame as py

from core.input import handle_input
from core.physics import update
from rendering.drawing import draw
from entities.camera import Camera
from constants import WIDTH, HEIGHT

class Game:
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode((WIDTH, HEIGHT), py.RESIZABLE)
        self.camera = Camera()

        self.width = WIDTH
        self.height = HEIGHT

        self.running = True

    def run(self):
        while self.running:
            handle_input(self)
            update(self)
            draw(self)
            py.display.flip()

        py.quit()