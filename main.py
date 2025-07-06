import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player1 = Player()
scoreboard1 = Scoreboard()
cars = []
screen.listen()
screen.onkey(player1.up, "w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if random.randint(1,3) == 1:
        cars.append(CarManager(STARTING_MOVE_DISTANCE))
    for i in cars:
        i.move_left()
        if player1.distance(i) < 20:
            scoreboard1.game_over()
            game_is_on = False
    if player1.ycor() >= 280:
        for i in cars:
            i.hideturtle()
            i.clear()
        cars = []
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        scoreboard1.increase_score()
        scoreboard1.update_scoreboard()
        player1.refresh()






screen.exitonclick()