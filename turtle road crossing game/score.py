from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.level=0
        self.score_display()
    def score_display(self):
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-220,250)
        self.output()
    def output(self):
        self.write(f"LEVEL:{self.level}",align='center',font=('Arial',20,'normal'))
    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write(f"Game_over",align='center',font=('Arial',14,'normal'))
        self.score_display()

    def increase_score(self):
        self.clear()
        self.level+=1
        self.score_display()


