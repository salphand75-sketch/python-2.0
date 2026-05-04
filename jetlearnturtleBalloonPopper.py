import turtle
import random
import time
turtle.colormode(255)
t = turtle.Turtle()
s = turtle.Screen()
badballoon = turtle.Turtle()
badballoon.pencolor("red")
badballoon.fillcolor("black")
badballoon.shape("circle")
showscore = turtle.Turtle()
showscore.up()
showscore.hideturtle()
showscore.goto(180,230)
score = 0
showscore.write("score = " + str(score),font=("Arial",15,"normal"))
s.setup(550,550)
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
def spawn_balloon():
    a = random.randint(20,235)
    b = random.randint(20,235)
    c = random.randint(20,235)
    balloon = turtle.Turtle()
    balloon.hideturtle()
    balloon.speed(0)
    balloon.shape("circle")
    balloon.color(a,b,c)
    balloon.up()
    x = random.randint(-250,250)
    balloon.goto(x,250)
    balloon.showturtle()
    balloonlist.append(balloon)
balloonlist = []
while True:
    
    timesp = random.randint(0,40)
    if timesp == 9:
        spawn_balloon()
    for balloon in balloonlist:
        balloon.sety(balloon.ycor()-5)
        if t.distance(balloon) < 20:
            balloon.hideturtle()
            balloonlist.remove(balloon)
            score = score + 1
            showscore.clear()
            showscore.write("score = " + str(score),font=("Arial",15,"normal"))
turtle.done()