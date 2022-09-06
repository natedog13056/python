from random import randint

apple = Actor('apple')
apple.pos = 400, 300

score = 0 # global variable

def draw(): # draw is a built-in function. called by engine by default
    screen.clear()
    apple.draw()

    screen.draw.text("Score: " + str(score), color="white", topleft=(10, 10))

def on_mouse_down(pos):
    global score # global reference firstly

    if apple.collidepoint(pos):
        print("Good Shot!")
        score += 1 # try to change value of a global variable
        place_apple()
    else:
        print("Missed Shot!")
        quit()

def place_apple():
    apple.pos = randint(10, 800), randint(10, 600)