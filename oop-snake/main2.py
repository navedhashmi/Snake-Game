import random
from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game!!")
screen.tracer(0)
screen.listen()
boa = Snake()
screen.onkey(key="a", fun=boa.turn_left)
screen.onkey(key="d", fun=boa.turn_right)
screen.onkey(key="w", fun=boa.turn_up)
screen.onkey(key="s", fun=boa.turn_down)
food = Food()
score = Scoreboard()

#a = boa.starting_positions
#print(a)

while True:
    screen.update()
    time.sleep(0.1)
    boa.move()
    if boa.head.distance(food) < 15:
        food.refresh()
        score.update_score()
        boa.add_segment(boa.segments[-1].pos())

    if boa.head.xcor() > 290 or boa.head.xcor() < -290 or boa.head.ycor() > 290 or boa.head.ycor() < -290:
        score.reset()
        boa.reset()
        #break
    for segments in boa.segments[1:]:
        #if segments == boa.head:
            #pass
        if boa.head.distance(segments) < 10:
            score.reset()
            boa.reset()
            #break
    else:
        continue
    break









screen.exitonclick()
