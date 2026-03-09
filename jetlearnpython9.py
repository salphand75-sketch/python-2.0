import turtle
import random
import time
t = turtle.Turtle()
s = turtle.Screen()
turtle.colormode(255)
s.bgcolor(0,0,0)
t.speed(0)
t.hideturtle()
for i in range(10):
    for i in range(3):
        color1 = random.randint(1,255)
        color2 = random.randint(1,255)
        color3 = random.randint(1,255)
        size = random.randint(30,70)
        t.color(color1,color2,color3)
        t.begin_fill()
        t.circle(size)
        t.end_fill()
        t.up()
        t.goto(random.randint(-230,230),random.randint(-230,230))
        t.down()
    time.sleep(0.5)
    t.clear()
turtle.done()
