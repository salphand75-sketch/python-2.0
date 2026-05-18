import turtle
import random
turtle.colormode(255)
t = turtle.Turtle()
s = turtle.Screen()
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
player_life1 = turtle.Turtle()
player_life1.up()
player_life1.goto(-250,250)
player_life1.speed(0)
player_life1.color("red")
player_life1.shape("arrow")
player_life2 = turtle.Turtle()
player_life2.up()
player_life2.goto(-238,250)
player_life2.speed(0)
player_life2.color("red")
player_life2.shape("arrow")
player_life3 = turtle.Turtle()
player_life3.up()
player_life3.goto(-226,250)
player_life3.speed(0)
player_life3.color("red")
player_life3.shape("arrow")
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

def spawn_badballoon():
    badballoon = turtle.Turtle()
    badballoon.hideturtle()
    badballoon.speed(0)
    badballoon.shape("circle")
    badballoon.pencolor("red")
    badballoon.fillcolor("black")
    badballoon.up()
    x = random.randint(-250,250)
    badballoon.goto(x,250)
    badballoon.showturtle()
    badballoonlist.append(badballoon)
badballoonlist = []
game_on = True
while game_on:  
    timespa = random.randint(0,80)
    if timespa == 9:
        spawn_badballoon()
    for badballoon in badballoonlist:
        badballoon.sety(badballoon.ycor()-5)
        if t.distance(badballoon) < 20:
            badballoon.hideturtle()
            badballoonlist.remove(badballoon)
            if player_life1.isvisible():
                player_life1.hideturtle()
            elif player_life2.isvisible():
                player_life2.hideturtle()
            elif player_life3.isvisible():
                player_life3.hideturtle()
                turtle.write("Game Over!",font=("arial",20,"bold"))
                turtle.hideturtle()
                game_on = False
                break
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
for badballoon in badballoonlist:
    badballoon.hideturtle()
for balloon in balloonlist:
    balloon.hideturtle()
t.hideturtle()
turtle.done()