from turtle import Turtle
FONT=("Courier", 20, "normal")
class ScoreBoard(Turtle):

    p1_score=0
    p2_score=0

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0,270)
        self.write("0 - 0",False,"center",FONT)

    def score(self):
        self.clear()
        self.write(f"{self.p2_score} - {self.p1_score}", False, "center", FONT)


