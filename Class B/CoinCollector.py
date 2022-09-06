from random import randint

fox = Actor("fox")
fox.pos = 400, 300

coin = Actor("coin")
coin.pos = 100, 100

score = 0               # integer variable holding the score value
game_over = False       # boolean variable indicating if game is over

WIDTH = 800
HEIGHT = 600

def draw(): # built-in function, called as entry of the game by engine automatically
    screen.fill('lightblue')

    if not game_over:
        fox.draw()
        coin.draw()

        screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))
    else:
        screen.draw.text("Final Score: " + str(score), color="black", topleft=(200, 300), fontsize=48)

def update(): # built-in function, called every 20ms by engine automatically, change states of object
    global score

    if keyboard.left:
        fox.x -= 3
    elif keyboard.right:
        fox.x += 3
    elif keyboard.up:
        fox.y -= 3
    elif keyboard.down:
        fox.y += 3

    # colliderect
    if fox.colliderect(coin):
        score += 1
        replace_coin()

def replace_coin():
    coin.pos = randint(0, WIDTH), randint(0, HEIGHT)

def time_up():
    global game_over

    game_over = True

# call the time_up function in 10 seconds
clock.schedule(time_up, 60)