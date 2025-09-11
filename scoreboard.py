from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.lives = 3
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.level}   Lives: {self.lives}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.write_score()

    def lose_life(self):
        self.lives -= 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)