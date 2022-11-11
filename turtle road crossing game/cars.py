from turtle import Turtle
import random

COLORS = ['red', 'green', "yellow", 'blue', 'orange', 'pink', 'violet']


class Cars():
    def __init__(self):
        self.all_cars = []
        self.speed=0.1

    def create_cars(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            c = Turtle()
            c.shape('square')
            c.penup()
            c.shapesize(1,2)
            c.color(random.choice(COLORS))
            y = random.randint(-250, 250)
            c.goto(300, y)
            self.all_cars.append(c)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(5)
    def increase_speed(self):
        self.speed*=0.9