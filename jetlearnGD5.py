import pgzrun
HEIGHT = 500
WIDTH = 500
drag = False
bear = Actor("bear.png")
"""def on_mouse_down(pos):
    global drag
    drag = True"""
def on_mouse_move(pos):
    bear.pos = (pos)
"""def on_mouse_up(pos):
    global drag
    drag = False"""
def draw():
    screen.blit("pgzbackground.jpg",(0,0))
    bear.draw()
pgzrun.go()