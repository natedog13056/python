# set the size of screen
from random import randint

WIDTH = 800
HEIGHT = 600

balloon = Actor('balloon')
balloon.pos = 400, 300

bird = Actor('bird-up')
bird.pos = randint(800, 1600), randint(10, 200)

house = Actor('house')
house.pos = randint(800, 1600), 460

tree = Actor('tree')
tree.pos = randint(800, 1600), 450

score = 0
''' global variable indicating if game is over '''
game_over = False

def draw():
    screen.blit('background', (0, 0))

    if game_over:
        screen.draw.text("Game Over! Final Score: " + str(score), (200, 250), color="black", fontsize=48)
    else:
        balloon.draw()
        bird.draw()
        house.draw()
        tree.draw()

        screen.draw.text("Score: " + str(score), (700, 5), color="black")

bird_up = True
count_of_update = 0

def flap():
    global bird_up, count_of_update

    count_of_update += 1

    if count_of_update % 5 == 0:
        if bird_up:
            bird.image = 'bird-down'
            bird_up = False
        else:
            bird.image = 'bird-up'
            bird_up = True

def update(): # this update function will be called every 60 ms  1s = 1000ms
    global game_over, score

    if not game_over:
        balloon.y += 1

        flap()

        bird.x -= 3
        house.x -= 1
        tree.x -= 1

        if bird.x < 0:
            bird.x = randint(800, 1600)
            score += 1

        if house.x < 0:
            house.x = randint(800, 1600)
            score += 1

        if tree.x < 0:
            tree.x = randint(800, 1600)
            score += 1

        ''' if balloon fly beyond the screen, game is over '''
        if balloon.y < 95 or balloon.y > 460:
            game_over = True

        ''' if balloon collide with tree, house or bird, game is over '''
        if balloon.collidepoint(bird.x, bird.y) or balloon.collidepoint(tree.x, tree.y) or balloon.collidepoint(house.x, house.y):
            game_over = True

def on_mouse_down():
    balloon.y -= 20