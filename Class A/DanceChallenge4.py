from random import randint

WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

score = 0

dancer = Actor('dancer-start')
dancer.pos = CENTER_X + 5, CENTER_Y - 40

up = Actor("up")
up.pos = CENTER_X, CENTER_Y + 110
right = Actor("right")
right.pos = CENTER_X + 60, CENTER_Y + 170
left = Actor("left")
left.pos = CENTER_X - 60, CENTER_Y + 170
down = Actor("down")
down.pos = CENTER_X, CENTER_Y + 230

# music.play('vanishing-horizon')

move_list = []
game_over = False
show_count_down = False
say_dance = False
moves_complete = True

count = 4
current_move = 0
score = 0

def draw():
    screen.clear()
    screen.blit("stage", (0, 0))

    if not game_over:
        dancer.draw()
        up.draw()
        right.draw()
        left.draw()
        down.draw()

        screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

        if show_count_down:
            screen.draw.text(str(count), color="black", topleft=(CENTER_X - 8, 150), fontsize=60)

        if say_dance:
            screen.draw.text("Let's Dance !", color="black", topleft=(CENTER_X - 130, 150), fontsize=60)
    else:
        screen.draw.text("Game Over ! " + str(score), color="black", topleft=(CENTER_X - 130, 150), fontsize=60)

def on_key_up(key):
    global say_dance, move_list, game_over, moves_complete, current_move, score

    say_dance = False

    if key == keys.UP:
        dancer_move = 0
    elif key == keys.RIGHT:
        dancer_move = 1
    elif key == keys.DOWN:
        dancer_move = 2
    elif key == keys.LEFT:
        dancer_move = 3

    update_dancer(dancer_move)

    if dancer_move == move_list[current_move]:
        current_move += 1
    else:
        game_over = True

    if current_move == 4:
        moves_complete = True
        current_move = 0
        score += 4

def resetAll():
    dancer.image = 'dancer-start'
    up.image = 'up'
    down.image = 'down'
    left.image = 'left'
    right.image = 'right'

def update_dancer(move):
    if move == 0:
        up.image = 'up-lit'
        dancer.image = 'dancer-up'
    elif move == 1:
        right.image = 'right-lit'
        dancer.image = 'dancer-right'
    elif move == 2:
        down.image = 'down-lit'
        dancer.image = 'dancer-down'
    elif move == 3:
        left.image = 'left-lit'
        dancer.image = 'dancer-left'

    clock.schedule(resetAll, 0.5)

def update():
    global game_over, moves_complete, current_move

    if not game_over:
        if moves_complete:
            generate_moves()
            moves_complete = False
            current_move = 0
    else:
        music.stop()

def generate_moves():
    global move_list, show_count_down

    move_list.clear()

    for move in range(0, 4):
        move_list.append(randint(0, 3))

    print(move_list)

    show_count_down = True
    count_down()

def count_down():
    global show_count_down, count

    if count > 1:
        count -= 1
        clock.schedule(count_down, 1)
        print("counting " + str(count))
    else:
        show_count_down = False
        count = 4

        display_moves()

def display_moves():
    global current_move, say_dance

    update_dancer(move_list[current_move])
    current_move += 1

    if current_move == 4:
        current_move = 0
        say_dance = True
    else:
        clock.schedule(display_moves, 1)

