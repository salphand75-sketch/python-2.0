import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.shapesize(0.7,0.7)
t.up()
t.goto(-176,176)
s = turtle.Screen()
s.setup(500,500)
t.speed(0)
foods = []
walls = []
maze = ["XXXXXXXXXXXXXXX",
        "X             X",
        "X X XXXXXXXXX X",
        "X X    X      X",
        "X XXXX XXXXX XX",
        "X  FX      X  X",
        "XXXXXXXXXX XX X",
        "X    XXF   X  X",
        "X XX  XXXXXX XX",
        "X XXX   X     X",
        "X   X X   XXXXX",
        "X X X XXXXX   X",
        "X X XXX   X X X",
        "XFX     X   X X",
        "XXXXXXXXXXXXXFX",]
for i in range(len(maze)):
    for j in range(len(maze[i])):
        x = -200 + (j*24)
        y = 200 - (i*24)
        if maze[i][j] == "X":
            wall = turtle.Turtle()
            wall.speed(0)
            wall.shape("square")
            wall.up()
            wall.goto(x,y)
            walls.append(wall)
        elif maze[i][j] == "F":
            food = turtle.Turtle()
            food.up()
            food.shape("circle")
            food.speed(0)
            food.color("red")
            food.goto(x,y)
            foods.append(food)
def check_wall(x,y):
    for wall in walls:
        if wall.xcor() == x and wall.ycor() == y:
            return True
    return False
def up():
    y = (t.ycor()+24)
    x = t.xcor()
    if check_wall(x,y) == False:
        t.sety(y)
    t.setheading(90)
    win()
s.listen()
s.onkey(up,"Up")
def right():
    x = (t.xcor()+24)
    y = t.ycor()
    if check_wall(x,y) == False:
        t.setx(x)
    t.setheading(0)
    win()
s.onkey(right,"Right")
def down():
    y = (t.ycor()-24)
    x = t.xcor()
    if check_wall(x,y) == False:
        t.sety(y)
    t.setheading(270)
    win()
s.onkey(down,"Down")
def left():
    x = (t.xcor()-24)
    y = t.ycor()
    if check_wall(x,y) == False:
        t.setx(x)
    t.setheading(180)
    win()
s.onkey(left,"Left")
def win():
    for food in foods:
        if t.distance(food) < 20:
            food.hideturtle()
            foods.remove(food)
    if not foods:
        print("You have eaten your food!")
turtle.done()