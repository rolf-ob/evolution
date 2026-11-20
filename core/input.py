import pygame as py

def update_camera(game, keys):
    if keys[py.K_w]:
        game.camera.y += 1
    if keys[py.K_a]:
        game.camera.x -= 1
    if keys[py.K_s]:
        game.camera.y -= 1
    if keys[py.K_d]:
        game.camera.x += 1

def handle_input(game):
    update_camera(game, py.key.get_pressed())
    
    for event in py.event.get():
        if event.type == py.QUIT:
            game.running = False

        elif event.type == py.VIDEORESIZE:
            game.width, game.height = event.size