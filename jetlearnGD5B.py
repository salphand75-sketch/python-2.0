import pgzrun
import random
HEIGHT = 350
WIDTH = 500
score = 0
unicorn = Actor("unicorn.png")
def on_mouse_down(pos):
    global score
    if unicorn.collidepoint(pos):
        score += 1
    else:
        score -= 1
def rpos():
    x = random.randint(50,450)
    y = random.randint(50,300)
    unicorn.pos = (x,y)
    clock.schedule(rpos,1)
def draw():
    screen.blit("waterfall.jpg",(0,0))
    unicorn.draw()
    screen.draw.text("score " + str(score),(400,10),color="black")
rpos()
pgzrun.go()