from random import randint

from pgzero.actor import Actor

WIDTH = 800
HEIGHT = 600

balloon = Actor("balloon")
balloon.pos = 400, 300

bird = Actor("bird-up")
bird.pos = randint(800, 1600), randint(10, 200)
house = Actor("house")
house.pos = randint(800, 1600), 460
tree = Actor("tree")
tree.pos = randint(800, 1600), 450

game_over = False
score = 0

up = False

def draw():
    screen.blit("background", (0, 0))

    if not game_over:
        balloon.draw()
        bird.draw()
        house.draw()
        tree.draw()

        screen.draw.text("Score: " + str(score), (700, 5), color="black")
    else:
        screen.draw.text("Final Score: " + str(score), (300, 300), color="black")

def on_mouse_down():
    global up
    up = True
    balloon.y -= 20

def on_mouse_up():
    global up
    up = False

def update():
    global game_over, score

    if not game_over:
        if not up:
            balloon.y += 1 # why it's 1 not 20 ?

        if bird.x > 0:
            bird.x -= 4
        else:
            score += 1
            bird.x = randint(800, 1600)
            bird.y = randint(10, 200)

        if house.x > 0:
            house.x -= 1 # why it's 1, not 4 ?
        else:
            score += 1
            house.x = randint(800, 1600)

        if tree.x > 0:
            tree.x -= 1 # why it's 1, not 4 ?
        else:
            score += 1
            tree.x = randint(800, 1600)

        if balloon.top < 0 or balloon.bottom > 560: # why not use y to compare ?
            game_over = True

        # collide point
        if balloon.collidepoint(bird.x, bird.y) or balloon.collidepoint(house.x, house.y) or balloon.collidepoint(tree.x, tree.y):
            game_over = True