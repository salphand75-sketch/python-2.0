import pgzrun
import random
HEIGHT = 800
WIDTH = 650
spaceship = Actor("spaceship.png")
spaceship.pos = (325, 700) 
aliens = []
bullets = []
healtreduction = 0

def alienspawn():
    for i in range(6):
        for j in range(10):
            alien = Actor("alien.png")
            alien.x = (j + 1) * 75 
            alien.y = i * 50 - 50
            aliens.append(alien)
    clock.schedule(alienspawn, 18)
alienspawn()
def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor("blaster.png")
        bullet.pos = (spaceship.x,spaceship.y -20)
        bullets.append(bullet)

def draw():
    screen.blit("space.jpg", (0, -100))
    for bullet in bullets:
        bullet.draw()
    spaceship.draw()
    for alien in aliens:
        alien.draw()
def update():
    if keyboard.a:
        spaceship.x -=5
    if keyboard.d:
        spaceship.x +=5
    for alien in aliens:
        alien.y += 0.5
    for bullet in bullets[:]:
        bullet.y -= 3
        if bullet.y < 0:
            bullets.remove(bullet)
        for alien in aliens[:]:
            if bullet.colliderect(alien) and alien in aliens and bullet in bullets:
                aliens.remove(alien)
                bullets.remove(bullet)
    
pgzrun.go()