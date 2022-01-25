import turtle

# stuff
turtle.bgcolor("black")
turtle.pencolor("white")
turtle.speed(20)
turtle.hideturtle()

# pp
# pp lines
turtle.penup()
turtle.goto(-50, -100)
turtle.pendown()
turtle.left(90)
turtle.forward(250)

turtle.penup()
turtle.goto(50, -100)
turtle.pendown()
turtle.forward(250)

# pp tip
# pp tip start
turtle.penup()
turtle.goto(-50, 150)
turtle.pendown()

tip_bend_1 = 0
while tip_bend_1 < 7:
    turtle.left(10)
    turtle.forward(1)
    tip_bend_1 = tip_bend_1 + 1
tip_bend_2 = 0
while tip_bend_2 < 10:
    turtle.right(11)
    turtle.forward(2)
    tip_bend_2 = tip_bend_2 + 1
# tip curve start
tip_bend_3 = 0
while tip_bend_3 < 12:
    turtle.forward(5)
    turtle.right(1)
    tip_bend_3 = tip_bend_3 + 1

turtle.penup()
turtle.goto(50, 150)
turtle.pendown()
turtle.left(55)

# pp tip start
tip_bend_1 = 0
while tip_bend_1 < 7:
    turtle.right(10)
    turtle.forward(1)
    tip_bend_1 = tip_bend_1 + 1
tip_bend_2 = 0
while tip_bend_2 < 10:
    turtle.left(11)
    turtle.forward(2)
    tip_bend_2 = tip_bend_2 + 1
tip_bend_3 = 0
# tip curve start
while tip_bend_3 < 12:
    turtle.forward(5)
    turtle.left(1)
    tip_bend_3 = tip_bend_3 + 1
tip_bend_4 = 0
while tip_bend_4 < 7:
    turtle.forward(4)
    turtle.left(11)
    tip_bend_4 = tip_bend_4 + 1

turtle.penup()
turtle.goto(-50, -100)
turtle.pendown()
turtle.left(48)

# lower pp
pp_bend_1 = 0
while pp_bend_1 < 26:
    turtle.left(3)
    turtle.forward(3)
    pp_bend_1 = pp_bend_1 + 1

turtle.penup()
turtle.goto(50, -100)
turtle.pendown()
turtle.right(78)

pp_bend_1 = 0
while pp_bend_1 < 28:
    turtle.right(3)
    turtle.forward(3)
    pp_bend_1 = pp_bend_1 + 1

# balls
# left ball
turtle.penup()
turtle.goto(-90, -110)
turtle.pendown()
turtle.circle(55)
# right ball
turtle.penup()
turtle.goto(80, -110)
turtle.pendown()
turtle.circle(55)

# more line stuff
turtle.penup()
turtle.goto(-50, 150)
turtle.pendown()
turtle.right(186)
turtle.forward(100)

turtle.penup()
turtle.goto(0, 150)
turtle.pendown()
turtle.left(90)
turtle.forward(68)

turtle.done()
