from random import randint

apple = Actor('apple')
apple.pos = 400, 300

score = 0
game_over = False

def draw():
    screen.clear()

    if game_over:
        screen.draw.text("Final Score: " + str(score), color='white', fontsize=48, topleft=(300, 300))
    else:
        apple.draw()

        screen.draw.text("Score: " + str(score), color='white', topleft=(10, 10))

def on_mouse_down(pos):
    global score, game_over

    if apple.collidepoint(pos):
        print("Good Shot!")
        score += 1
        place_apple()
    else:
        print("Missed Shot!")
        #quit()
        game_over = True

def place_apple():
    apple.pos = randint(10, 800), randint(10, 600)