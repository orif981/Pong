from turtle import Turtle
from scoreboard import ScoreBoard

scoreboard=ScoreBoard()
class Ball(Turtle):
    X_MOVEMENT = 2
    Y_MOVEMENT = 2

    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.color("white")

    def move(self):
        self.goto(self.xcor()+self.X_MOVEMENT,self.ycor()+self.Y_MOVEMENT)

    def up_down_wall(self):
        self.Y_MOVEMENT*=-1

    def bounce(self):
        self.X_MOVEMENT*=-1

    def player2_won(self):
        self.goto(0,0)
        self.X_MOVEMENT,self.Y_MOVEMENT=-2,-2
        scoreboard.p2_score+=1

    def player1_won(self):
        self.goto(0, 0)
        self.X_MOVEMENT, self.Y_MOVEMENT = 2, 2
        scoreboard.p1_score += 1