import random
from turtle import Turtle
from random import Random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, STARTING_MOVE_DISTANCE):
        super().__init__()
        self.shape("square")
        self.shapesize(1,2)
        self.penup()
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.movingdistance = STARTING_MOVE_DISTANCE
        self.setpos(300, random.randrange(-260,260))
    def move_left(self):
        self.goto(self.xcor() - self.movingdistance, self.ycor())
