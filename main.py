from turtle import *
from paddle import Paddle
from ball import Ball,scoreboard
import time


screen=Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")
screen.listen()

player1=Paddle()
player2=Paddle(-350)
ball=Ball()

screen.onkey(player1.up, "Up")
screen.onkey(player1.down, "Down")
screen.onkey(player2.up, "w")
screen.onkey(player2.down, "s")

time_sleep=0.01
game_on=True
while game_on:
    print(time_sleep)
    screen.update()
    ball.move()
    time.sleep(time_sleep)

    if ball.ycor()>290 or ball.ycor()<-280:
        ball.up_down_wall()

    if ball.xcor()==330:
        print(3)
        if ball.distance(player1)<50:
            print(4)
            ball.bounce()
            time_sleep *= 0.01

    elif ball.xcor()==-330:
        print(2)
        if ball.distance(player2)<50:
            print(1)
            ball.bounce()
            time_sleep*=0.01

    if ball.xcor()>390:
        ball.player2_won()
        time_sleep=0.01
    elif ball.xcor()<-390:
        ball.player1_won()
        time_sleep = 0.01

    scoreboard.score()


screen.exitonclick()

if __name__ == '__main__':
    pass


