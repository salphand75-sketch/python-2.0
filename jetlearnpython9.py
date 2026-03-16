import turtle
import random
t = turtle.Turtle()
s = turtle.Screen()
turtle.colormode(255)
t.shape("circle")
t.up()
t.goto(-230,0)
t.left(90)
for i in range(4):
    color1 = random.randint(0,255)
    color2 = random.randint(0,255)
    color3 = random.randint(0,255)
    t.color(color1,color2,color3)
    for i in range(18):
        t.forward(10)
        t.right(10)
    t.left(180)
for i in range(4):
    color1 = random.randint(0,255)
    color2 = random.randint(0,255)
    color3 = random.randint(0,255)
    t.color(color1,color2,color3)
    for i in range(18):
        t.forward(10)
        t.left(10)
    t.right(180)