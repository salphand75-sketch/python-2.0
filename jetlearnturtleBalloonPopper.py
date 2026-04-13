import turtle
import random
t = turtle.Turtle()
s = turtle.Screen()
s.setup(500,500)
t.color("red")
t.shape("triangle")
t.right(30)
t.up()
t.goto(-10,-200)
s.listen()
def right():
    x = (t.xcor()+25)
    y = t.ycor()
    if x < 250:
        t.goto(x,y)
s.onkey(right,"Right")
def left():
    x = (t.xcor()-25)
    y = t.ycor()
    if x > -250:
        t.goto(x,y)
s.onkey(left,"Left")
balloon = turtle.Turtle()
balloon.up()
x = random.randint(-250,250)
balloon.goto(x,250)
while True:
    balloon.goto(x,t.ycor()-5)





turtle.done()