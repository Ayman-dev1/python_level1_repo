import turtle

window = turtle.Screen()
window.title("Ping Pong By Ayman")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)  # stops the window from updating automatically

# madrab1
madrab1 = turtle.Turtle()  # initializes turtle object(shape)
madrab1.speed(0)  # set the speed of the animation
madrab1.shape("square")  # set the shape of the object
madrab1.color("blue")  # set the color of the shape
madrab1.shapesize(stretch_wid=5, stretch_len=1)  # stretches the shape to meet the size
madrab1.penup()  # stops the object from drawing lines
madrab1.goto(-350, 0)  # set the position of object

#madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()
madrab2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("White")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 | Player 2: 0", align="center", font=("Courier", 24, "normal"))


#functions
def madrab1_up():
    y = madrab1.ycor()  # get the y coordinate of the madrab1
    y += 20  # set the y to increase by 20
    madrab1.sety(y)  # set the y of the madrab1 to the new y coordinate


def madrab1_down():
    y = madrab1.ycor()
    y -= 20
    madrab1.sety(y)


def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)


def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)


# keyboard bindings
window.listen()  # tell the window to expect keyboard input
window.onkeypress(madrab1_up, "w")  # when pressing w the function madrab1_up is invoked
window.onkeypress(madrab1_down, "s")
window.onkeypress(madrab2_up, "Up")
window.onkeypress(madrab2_down, "Down")

# main game loop
while True:
    window.update()  # updates the screen every time the loop run

    # move the ball
    ball.setx(ball.xcor() + ball.dx)  # ball starts at 0 and everytime loops run ----> +0.2 xaxis
    ball.sety(ball.ycor() + ball.dy)  # ball starts at 0 and everytime loops run ----> +0.2 yaxis

    # border check , top border +300px, bottom border -300px, ball is 20px
    if ball.ycor() > 290:  # if ball is at top border
        ball.sety(290)  # set y coordinate +290
        ball.dy *= -1  # reverse direction, making +0.3-----> -0.3

    if ball.ycor() < -290:  # if ball is at bottom border
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:  # if ball is at right border
        ball.goto(0, 0)  # return ball to center
        ball.dx *= -1  # reverse the x direction
        score1 += 1
        score.clear()
        score.write("Player 1: {} | Player 2: {}".format(score1, score2), align="center",
                    font=("Courier", 24, "normal"))

    if ball.xcor() < -390:  # if ball is at left border
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {} | Player 2: {}".format(score1, score2), align="center",
                    font=("Courier", 24, "normal"))

    # tasadom ball with madrab
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
