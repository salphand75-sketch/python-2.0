import pgzrun
HEIGHT = 500
WIDTH = 500
def draw():
    screen.blit("pgzbackground.jpg",(0,0))
    screen.blit("bear.png",(250,250))
pgzrun.go()