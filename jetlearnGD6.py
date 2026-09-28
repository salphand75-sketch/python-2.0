import pgzrun
import random

game_over = False
HEIGHT = 500
WIDTH = 500
score = 0

mouse = Actor("mouse.png")
cat = Actor("2d_cat.png")
cheese = Actor("cheese.png")
mouse.pos = (250,250)
cat.pos = (250, 250)
curser = (0,0)
dirx = random.randint(-1,1)
diry = random.randint(-1,1)
speed = 3
def update():

    global score,dirx,diry
    if mouse.colliderect(cat):
            game_over = True
    mouse.x = mouse.x+(curser[0]-mouse.x)*0.025
    mouse.y = mouse.y+(curser[1]-mouse.y)*0.025
    if mouse.colliderect(cheese):
         score += 1
         cheese.pos = (random.randint(50,450),random.randint(50,450))
    cat.x += speed*dirx
    cat.y += speed*diry
    if cat.x >= 450:
         dirx = -1
    if cat.x <= 0:
         dirx = 1
    if cat.y <= 0:
         diry = 1
    if cat.y >= 450:
         diry = -1
def on_mouse_move(pos):
    global curser
    if not game_over:
        curser = pos

def draw():
    screen.blit("pgzbackground.jpg",(0,0))
    mouse.draw()
    cat.draw()
    cheese.draw()
    screen.draw.text("score " + str(score),(400,10),color="black")
pgzrun.go()