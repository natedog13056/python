WIDTH = 1280
HEIGHT = 700

plane = Actor('game_character')
plane.pos = WIDTH / 2, HEIGHT / 2

def draw():
    screen.blit('background', (0, 0))

    plane.draw()