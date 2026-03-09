import turtle
import random
t = turtle.Turtle()
s = turtle.Screen()
t.speed(0)
t.shape("circle")
turtle.colormode(255)
t.up()
while True:
    color1 = random.randint(0,255)
    color2 = random.randint(0,255)
    color3 = random.randint(0,255)
    t.color(color1,color2,color3)
    t.forward(5)
    t.right(10)
    