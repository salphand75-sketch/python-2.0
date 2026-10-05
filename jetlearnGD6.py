import pgzrun
import random

game_over = False
HEIGHT = 500
WIDTH = 600
score = 0
reset = Actor("reset.png")
mouse = Actor("mouse.png")
cat = Actor("2d_cat.png")
cheese = Actor("cheese.png")
mouse.pos = (250,250)
cat.pos = (50, 50)
reset.pos = (260,400)
curser = (0,0)
dirx = random.randint(-1,1)
diry = random.randint(-1,1)
speed = 3
def update():
    global score,dirx,diry,game_over
    if mouse.colliderect(cat):
            game_over = True
            return
    mouse.x = mouse.x+(curser[0]-mouse.x)*0.025
    mouse.y = mouse.y+(curser[1]-mouse.y)*0.025
    if mouse.colliderect(cheese):
         score += 1
         cheese.pos = (random.randint(50,450),random.randint(50,450))
    cat.x += speed*dirx
    cat.y += speed*diry
    if cat.x >= WIDTH - 50:
         dirx = -1
         diry = random.randint(-1,1)
    if cat.x <= 0:
         dirx = 1
         diry = random.randint(-1,1)
    if cat.y <= 0:
         diry = 1
         dirx = random.randint(-1,1)
    if cat.y >= HEIGHT:
         diry = -1
         dirx = random.randint(-1,1)
def on_mouse_move(pos):
    global curser
    if not game_over:
        curser = pos
def on_mouse_down(pos):
     global score,mouse,cat,curser,dirx,diry,game_over
     if reset.collidepoint(pos): 
         game_over = False
         score = 0
         mouse.pos = (pos)
         cat.pos = (50, 50)
         curser = (0,0)
         dirx = random.randint(-1,1)
         diry = random.randint(-1,1)
speed = 3
def draw():
    screen.blit("pgzbackground.jpg",(0,0))
    if game_over == True:
         screen.blit("game_over.png",(50,75))
         screen.draw.text("Your score: " + str(score),(240,300),color="black", fontsize =30)
         reset.draw()
         return
    mouse.draw()
    cat.draw()
    cheese.draw()
    screen.draw.text("score: " + str(score),(450,10),color="black")
pgzrun.go()