import turtle
import random
import time

# Setup window
wn = turtle.Screen()
wn.title("computer graffics Project")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

colors = ["red", "blue", "green", "yellow"]

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)
paddle.color("red")

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.penup()
ball.goto(0, 250)
ball.color(random.choice(colors))
ball.dy = -3

# Score
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.color("white")
score_display.penup()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Arial", 16, "bold"))

# Paddle movement
def move_left():
    x = paddle.xcor()
    if x > -250:
        paddle.setx(x - 30)

def move_right():
    x = paddle.xcor()
    if x < 250:
        paddle.setx(x + 30)

# Change paddle color
def change_color():
    new_color = random.choice(colors)
    paddle.color(new_color)

wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(change_color, "space")

# Game loop
game_over = False

while not game_over:
    wn.update()
    time.sleep(0.01)

    ball.sety(ball.ycor() + ball.dy)

    # Ball hits bottom
    if ball.ycor() < -300:
        ball.goto(random.randint(-250, 250), 250)
        ball.color(random.choice(colors))

    # Catch detection
    if (ball.ycor() < -230 and ball.ycor() > -260) and \
       (paddle.xcor() - 60 < ball.xcor() < paddle.xcor() + 60):

        if ball.color()[0] == paddle.color()[0]:
            score += 1
            ball.dy -= 0.2  # increase difficulty
            score_display.clear()
            score_display.write(f"Score: {score}", align="center",
                                font=("Arial", 16, "bold"))
            ball.goto(random.randint(-250, 250), 250)
            ball.color(random.choice(colors))
        else:
            game_over = True

# Game Over message
score_display.goto(0, 0)
score_display.write("GAME OVER", align="center",
                    font=("Arial", 24, "bold"))

wn.mainloop()
