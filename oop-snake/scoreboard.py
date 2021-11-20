from turtle import Turtle
from os import path


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as highscore:
            self.highscore = int(highscore.read())
        print(self.highscore)
        self.clear()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score : {self.score} High-Score : {self.highscore}", align="center", font=("Arial", 15, "normal"))
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High-Score : {self.highscore}", align="center", font=("Arial", 15, "normal"))

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as highscore:
                highscore.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    #def game_over(self):
        #self.goto(0, 0)
        #self.write(f"Game Over | Final Score {self.score}", align="center", font=("Arial", 20, "normal"))

