from random import randint

WIDTH = 800
HEIGHT = 600

CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

dancer = Actor("dancer-start")
dancer.pos = CENTER_X + 5, CENTER_Y - 40

music.play('vanishing-horizon')

up = Actor('up')
up.pos = CENTER_X, CENTER_Y + 110
right = Actor('right')
right.pos = CENTER_X + 60, CENTER_Y + 170
down = Actor('down')
down.pos = CENTER_X, CENTER_Y + 230
left = Actor('left')
left.pos = CENTER_X - 60, CENTER_Y + 170

move_list = []
current_move = 0
moves_complete = True
game_over = False

score = 0
say_dance = False

def draw():
    screen.clear()
    screen.blit('stage', (0, 0))

    if not game_over:
        dancer.draw()
        up.draw()
        right.draw()
        down.draw()
        left.draw()

        screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

        if say_dance:
            screen.draw.text("Let's Dance !", color="black", topleft=(CENTER_X - 130, 150), fontsize=60)
    else:
        screen.draw.text("Final Score: " + str(score), color="black", topleft=(CENTER_X - 130, 150), fontsize=60)

def update():
    global moves_complete, current_move

    if not game_over:
        if moves_complete:
            generate_moves()
            moves_complete = False
            current_move = 0
    else:
        music.stop()

def on_key_up(key): # built-in function called when any key in the keyboard is pressed and released
    # press UP, DOWN, LEFT and RIGHT to change the dancer
    global say_dance, current_move, game_over, moves_complete, score

    say_dance = False

    if key == keys.UP:
        dancer_move = 0
    if key == keys.DOWN:
        dancer_move = 2
    if key == keys.LEFT:
        dancer_move = 3
    if key == keys.RIGHT:
        dancer_move = 1

    update_dancer(dancer_move)
    print(dancer_move, current_move, move_list[current_move])
    if dancer_move == move_list[current_move]:
        current_move += 1
    else:
        game_over = True

    if current_move == 4:
        moves_complete = True
        current_move = 0
        score += 4

def update_dancer(move):
    if move == 0:
        dancer.image = 'dancer-up'
        up.image = 'up-lit'
    elif move == 1:
        dancer.image = 'dancer-right'
        right.image = 'right-lit'
    elif move == 2:
        dancer.image = 'dancer-down'
        down.image = 'down-lit'
    elif move == 3:
        dancer.image = 'dancer-left'
        left.image = 'left-lit'

    clock.schedule(resetAll, 0.5)

def resetAll():
    dancer.image = 'dancer-start'
    up.image = 'up'
    down.image = 'down'
    left.image = 'left'
    right.image = 'right'

def generate_moves():
    global move_list

    move_list.clear()
    for move in range(0, 4):
        move_list.append(randint(0, 3))

    print(move_list)

    clock.schedule(display_moves, 1)

def display_moves():
    global current_move, say_dance

    update_dancer(move_list[current_move])

    current_move += 1

    if current_move == 4:
        current_move = 0
        say_dance = True
    else:
        clock.schedule(display_moves, 1)

