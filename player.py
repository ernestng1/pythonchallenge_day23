from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.setpos(STARTING_POSITION)
    def refresh(self):
        self.teleport(STARTING_POSITION[0],STARTING_POSITION[1])
    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
