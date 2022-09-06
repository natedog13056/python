from random import randint

from pgzero.actor import Actor
from pgzero.clock import clock
from pgzero.keyboard import keyboard
from pgzero.loaders import sounds

WIDTH = 1280
HEIGHT = 700

plane = Actor('plane_6')
plane.pos = 30, HEIGHT / 2

bullets = []
aliens = []
explosions = []
reward_list = []

# music.play('battleship')
score = 0

game_over = False
weapon_level = 1


def draw():
    screen.blit('background', (0,0))

    if game_over:
        screen.draw.text("Game Over ! Final Score: " + str(score), color="white", topleft=(450, 300), fontsize=48)
    else:
        plane.draw()

        for bullet in bullets:
            bullet.draw()

        for alien in aliens:
            alien.draw()

        for explosion in explosions:
            explosion.draw()
            explosions.remove(explosion)

        for reward in reward_list:
            reward.draw()

        screen.draw.text("Score: " + str(score), color="white", topleft=(10,10))


def update():
    global score, game_over, weapon_level

    if keyboard.left:
        if plane.x > 15:
            plane.x -= 5
    elif keyboard.right:
        if plane.x < WIDTH - 10:
            plane.x += 5
    elif keyboard.up:
        if plane.y > 15:
            plane.y -= 5
    elif keyboard.down:
        if plane.y < HEIGHT - 10:
            plane.y += 5

    for bullet in bullets:
        bullet.x += 6

    for alien in aliens:
        alien.x -= 6

    for reward in reward_list:
        reward.x -= 3

        if reward.colliderect(plane):
            weapon_level += 1
            reward_list.remove(reward)

    for alien in aliens:
        for bullet in bullets:
            if alien.colliderect(bullet):
                score += 1

                bullets.remove(bullet)
                aliens.remove(alien)

                explosion = Actor('explosion', (alien.x, alien.y))
                explosions.append(explosion)
                sounds.explode.play()

        if alien.colliderect(plane):
            game_over = True


def on_key_up(key):
    if key == keys.SPACE:
        sounds.pew.play()

        if weapon_level == 1:
            bullet = Actor('bullet', (plane.x + 10, plane.y))
            bullets.append(bullet)
        elif weapon_level == 2:
            bullet = Actor('missile_1', (plane.x + 10, plane.y))
            bullets.append(bullet)
        else:
            bullet1 = Actor('missile_1', (plane.x + 10, plane.y - 10))
            bullet2 = Actor('missile_1', (plane.x + 10, plane.y + 10))
            bullets.append(bullet1)
            bullets.append(bullet2)


def add_alien():
    alien = Actor('alien_1', (WIDTH + 10, randint(20, HEIGHT - 20)))
    aliens.append(alien)


clock.schedule_interval(add_alien, 1)


def add_reward():
    reward = Actor('star', (WIDTH + 10, randint(20, HEIGHT - 20)))
    reward_list.append(reward)


clock.schedule_interval(add_reward, 10)

