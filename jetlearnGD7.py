import pgzrun
import random

HEIGHT = 800
WIDTH = 650

spaceship = Actor("spaceship.png")
spaceship.pos = (325, 700) 

score = 0
aliens = []
bullets = []
alien_bullets = []

healthreduction = 0 
hearts_left = 3
heart1 = Actor("heart.png")
heart1.pos = (20,20)
heart2 = Actor("heart.png")
heart2.pos = (50,20)
heart3 = Actor("heart.png")
heart3.pos = (80,20)
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
        bullet.pos = (spaceship.x, spaceship.y - 20)
        bullets.append(bullet)

def alien_shoot():
    if  hearts_left >0:
        shooter = random.choice(aliens)
        alien_bullet = Actor("blaster2.png") 
        alien_bullet.pos = shooter.pos
        alien_bullets.append(alien_bullet)
    clock.schedule(alien_shoot, 3)


def draw():
    screen.blit("space.jpg", (0, -100))
    for bullet in bullets:
        bullet.draw()
    for alien_bullet in alien_bullets:
        alien_bullet.draw()
    if hearts_left >0:
        spaceship.draw()
    for alien in aliens:
        alien.draw()
    if hearts_left == 3:
        heart1.draw()
        heart2.draw()
        heart3.draw()
    elif hearts_left ==2:
        heart1.draw()
        heart2.draw()
    elif hearts_left ==1:
        heart1.draw()
    if hearts_left == 0:
        screen.blit("space.jpg", (0, -100))
        spaceship.draw()
        screen.blit("game_over.png",(50,75))   
        return 
    screen.draw.text("Your score: " + str(score),(450,30),color="white", fontsize =30)
        

def update():
    global healthreduction, hearts_left, score
    if hearts_left == 0:
        return     
    if keyboard.a and spaceship.x > 25:
        spaceship.x -= 5
    if keyboard.d and spaceship.x < WIDTH - 25:
        spaceship.x += 5 
    for alien in aliens:
        alien.y += 0.5
        if alien.y > HEIGHT:
            aliens.remove(alien)
            healthreduction += 1
            if healthreduction == 10:
                hearts_left = hearts_left - 1
                healthreduction = 0
    
    for bullet in bullets[:]:
        bullet.y -= 3
        if bullet.y < 0:
            bullets.remove(bullet)
            continue
        for alien in aliens[:]:
            if bullet.colliderect(alien) and alien in aliens and bullet in bullets:
                aliens.remove(alien)
                bullets.remove(bullet)
                score += 100
    for alien_bullet in alien_bullets[:]:
        alien_bullet.y += 4
        if alien_bullet.y > HEIGHT:
            alien_bullets.remove(alien_bullet)
            continue
        if alien_bullet.colliderect(spaceship):
            alien_bullets.remove(alien_bullet)
            hearts_left = hearts_left - 1
alien_shoot()
pgzrun.go()