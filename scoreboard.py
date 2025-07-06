from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.speed(0)
        self.penup()
        self.teleport(-280, 230)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Level:  {self.score}", False, "left", FONT)

    def game_over(self):
        self.clear()
        self.write(f"Game Over: Level {self.score}", False, "left", FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
