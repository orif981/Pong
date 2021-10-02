from turtle import Turtle,Screen




class Paddle(Turtle):

    def __init__(self, x_pos=350):
        super().__init__()
        self.pu()
        self.setx(x_pos)
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)


    def up(self):
        self.goto(self.xcor(),self.ycor()+20)


    def down(self):
        self.goto(self.xcor(),self.ycor()-20)

