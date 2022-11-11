from turtle import Turtle

SPEED = 20
Right = 0
LEFT = 180
DOWN = 270
UP = 90


class Body(Turtle):
    def __init__(self):
        super(Body, self).__init__()
        self.color('white')
        self.shape('turtle')
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def up(self):
        self.setheading(UP)
        self.forward(SPEED)

    def down(self):
        y = self.ycor() - SPEED
        self.goto(self.xcor(), y)

    def right_turn(self):
        r = self.xcor() + SPEED
        self.goto(r, self.ycor())

    def left_turn(self):
        l = self.xcor() - SPEED
        self.goto(l, self.ycor())
    def reset_position(self):
        self.goto(0,-280)
