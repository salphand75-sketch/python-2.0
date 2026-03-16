import turtle
t = turtle.Turtle()
food = turtle.Turtle()
s = turtle.Screen()
s.setup(500,500)
t.speed(0)
maze = ["XXXXXXXXXXXXXXX ",
        "X             X ",
        "X X XXXXXXXXX X ",
        "X X    X      X ",
        "X XXXX XXXXX XX ",
        "X   X      X  X ",
        "XXXXXXXXXX XX X ",
        "X     X    X  X ",
        "X XX  XXXXXX XX ",
        "X XXX   X     X ",
        "X   X X   XXXXX ",
        "X X X XXXXX   X ",
        "X X XXX   X X X ",
        "X X     X   X X ",
        "XXXXXXXXXXXXXFX ",]
for i in range(len(maze)):
    for j in range(len(maze[i])):
        x = -200 + (j*25)
        y = 200 - (i*25)
        if maze[i][j] == "X":
            wall = turtle.Turtle()
            wall.speed(0)
            wall.shape("square")
            wall.up()
            wall.goto(x,y)
        elif maze[i][j] == "F":
            food.up()
            food.shape("circle")
            food.color("green")
            food.goto(x,y)
turtle.done()
