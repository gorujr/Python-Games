import turtle

wn = turtle.Screen()
wn.title("Pong by @ aditya")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # Stops window from updating

# Scores
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # Set to maximum possible speed
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # stretching the paddle
paddle_a.penup()  # draw to a line _ Stop
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # Set to maximun possible speed
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # strehing the paddle
paddle_b.penup()  # draw to a line _ Stop
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)  # Set to maximum possible speed
ball.shape("circle")
ball.color("red")
ball.penup()  # draw to a line _ Stop
ball.goto(0, 0)
ball.dx = 0.05
ball.dy = 0.05

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0    Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function to move the Paddle
def paddle_a_up():
    y = paddle_a.ycor()
    y = y + 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y = y - 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y = y + 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y = y - 20
    paddle_b.sety(y)



# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, 'q')
wn.onkeypress(paddle_a_down, 'a')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, "Down")

# Main Loop Game
while True:
    wn.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy=ball.dy*-1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy=ball.dy*-1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = ball.dx*-1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = ball.dx*-1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and Ball collision
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx*= -1

    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1


