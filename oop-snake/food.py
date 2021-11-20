from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def refresh(self):
        self.penup()
        self.goto(random.randrange(-280, 280), random.randrange(-280, 280))