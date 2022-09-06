from random import randint

from pgzero import music
from pgzero.keyboard import keyboard
from pgzero.actor import Actor

WIDTH = 1280
HEIGHT = 700

plane = Actor("plane_small")
plane.pos = 50, 300

music.play('bg')

missiles = []
explosions = []
enemies = []
bombs = []
stars = []
trumps = []

score = 0
hold_fire = 0
game_over = False
game_over_sound_played = False
missile_count = 1

def draw():
    global game_over_sound_played

    screen.clear()

    screen.blit("bg", (0, 0))

    if game_over:
        screen.draw.text("Game Over! Final Score: " + str(score), color="white", topleft=(450, 300), fontsize=48)

        music.stop()

        if not game_over_sound_played:
            sounds.bomb.play()
            game_over_sound_played = True
    else:
        plane.draw()

        for bomb in bombs:
            bomb.draw()

        for missile in missiles:
            missile.draw()

        for enemy in enemies:
            enemy.draw()

        for trump in trumps:
            trump.draw()

        for explosion in explosions:
            explosion.draw()
            explosions.remove(explosion)

        screen.draw.text("Score: " + str(score), color="white", topleft=(10, 10))

def update():
    global score, game_over, hold_fire, missile_count

    hold_fire += 1

    if game_over:
        return

    if keyboard.up:
        if plane.y > 25:
            plane.y -= 5
    elif keyboard.down:
        if plane.y < HEIGHT - 25:
            plane.y += 5

    for bomb in bombs:
        if bomb.x < 0:
            bombs.remove(bomb)
        else:
            bomb.x -= 2

    for trump in trumps:
        if trump.x < 0:
            trumps.remove(trump)
        else:
            trump.x -= 2

    for missile in missiles:
        if missile.x > WIDTH:
            missiles.remove(missile)
        else:
            missile.x += 5

    for enemy in enemies:
        if enemy.x < 0:
            enemies.remove(enemy)
        else:
            enemy.x -= 4

    for enemy in enemies:
        if enemy.colliderect(plane):
            game_over = True
            return

        for missile in missiles:
            if missile.colliderect(enemy):
                explosion = Actor('explosion')
                explosion.pos = enemy.pos
                explosions.append(explosion)

                missiles.remove(missile)
                enemies.remove(enemy)

                sounds.explode.play()
                score += 1

    for bomb in bombs:
        if bomb.colliderect(plane):
            bombs.remove(bomb)
            destroy_all()

    for trump in trumps:
        if trump.colliderect(plane):
            trumps.remove(trump)
            missile_count += 1
            sounds.boo.play()

def destroy_all():
    global score

    for enemy in enemies:
        explosion = Actor('explosion', enemy.pos)
        explosions.append(explosion)

    score += len(enemies)
    enemies.clear()
    sounds.explode.play()

def on_key_up(key):
    global  hold_fire

    if key == keys.SPACE:
        if hold_fire > 20:
            if missile_count == 1:
                missiles.append(Actor('missile', (plane.x + 20, plane.y)))
            else:
                missiles.append(Actor('missile', (plane.x + 20, plane.y - 10)))
                missiles.append(Actor('missile', (plane.x + 20, plane.y + 10)))

            sounds.pew.play()
            hold_fire = 0

def add_alien():
    alien = Actor("alien")
    alien.pos= WIDTH + 10, randint(20, HEIGHT - 20)
    enemies.append(alien)
    clock.schedule(add_alien, randint(1, 3))

clock.schedule(add_alien, randint(1, 3))

def add_ufo():
    ufo = Actor("ufo")
    ufo.pos= WIDTH + 10, randint(20, HEIGHT - 20)
    enemies.append(ufo)

clock.schedule_interval(add_ufo, 5)

def add_bomb():
    bomb = Actor("rocket-bomb", (WIDTH + 10, randint(20, HEIGHT - 20)))
    bomb.angle = -45
    bombs.append(bomb)

clock.schedule_interval(add_bomb, 10)

def add_trump():
    trump = Actor("trump", (WIDTH + 10, randint(20, HEIGHT - 20)))
    trumps.append(trump)

clock.schedule_interval(add_trump, 20)

