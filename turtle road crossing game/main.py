import time
from cars import Cars
from turtle import Screen
from tutorize import Body
from score import Score
screen=Screen()
screen.setup(600,600)
screen.title('TURTLE RACING GAME')
screen.bgcolor('black')
screen.tracer(0)
player=Body()
cars=Cars()
score=Score()
screen.listen()
screen.onkey(fun=player.up, key='Up')
screen.onkey(fun=player.down, key='Down')
screen.onkey(player.right_turn, "Right")
screen.onkey(player.left_turn, 'Left')
game=True


while game:
    time.sleep(cars.speed)
    screen.update()
    cars.create_cars()
    cars.move_cars()
    for car in cars.all_cars:
        if car.distance(player)<14:
            game=False
            score.game_over()
    if player.ycor()>290:
        score.increase_score()
        player.reset_position()
        cars.increase_speed()
screen.exitonclick()