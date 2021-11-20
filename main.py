import random
from turtle import Turtle, Screen
import time


def snake_body(length):
    x = 0
    y = 0
    for _ in range(length):
        if _ == 0:
            viper = Turtle("head_east.gif")
        else:
            viper = Turtle("body_c.gif")
        #viper.color("white")
        viper.penup()
        viper.goto(x, y)
        snake.append(viper)
        x -= 20
    #snake[-1].shape("tail_hori.gif")


def snake_head():
    snake_head_1[0] = snake[0].pos()
    return snake_head_1[0]


def move_forward():
    head = snake_head()
    snake[0].fd(20)
    boa = []
    for x in range(1, snake_length[0]):
        boa.append(snake[x].pos())
        #if int(snake[0].heading()) == 0 or int(snake[0].heading()) == 180:
            #snake[x].shape("body_hori.gif")
        #else:
            #snake[x].shape("body_vert.gif")
        snake[x].goto(head)
        head = boa[-1]
        #screen.update()
    screen.update()
    return boa


def turn_left():
    print(snake[0].heading())
    if int(snake[0].heading()) == 0:
        snake[0].shape("head_north.gif")
    elif snake[0].heading() == 90:
        snake[0].shape("head_west.gif")
    elif snake[0].heading() == 180:
        snake[0].shape("head.gif")
    else:
        snake[0].shape("head_east.gif")
    #for x in range(1, len(snake)):
        #print(snake[x].heading())
        #if int(snake[0].heading()) == 0 or int(snake[0].heading()) == 180:
            #snake[x].shape("body_vert.gif")
        #else:
            #snake[x].shape("body_hori.gif")
    snake[0].left(90)
    move_forward()


def turn_right():
    print(snake[0].heading())
    if int(snake[0].heading()) == 180:
        snake[0].shape("head_north.gif")
    elif snake[0].heading() == 270:
        snake[0].shape("head_west.gif")
    elif snake[0].heading() == 0:
        snake[0].shape("head.gif")
    else:
        snake[0].shape("head_east.gif")
    snake[0].right(90)
    move_forward()


def score():
    scoreboard = Turtle()
    scoreboard.penup()
    scoreboard.goto(0, 280)
    style = ("Ariel", 15, "bold")
    scoreboard.write(f"Score :", font=style, align="center")


def points_system():
    points_player.undo()
    points_player.penup()
    points_player.goto(60, 280)
    global points
    points += 1
    points_player.write(f"{points}", font=style, align="right")

screen = Screen()
screen.setup(600, 600)
#screen.bgcolor("black")
screen.bgpic("grass.gif")
screen.register_shape("head_east.gif")
screen.register_shape("head_north.gif")
screen.register_shape("head_west.gif")
screen.register_shape("head.gif")
screen.register_shape("body_hori.gif")
screen.register_shape("body_vert.gif")
screen.register_shape("food.gif")
screen.register_shape("body_c.gif")
#screen.register_shape("tail_hori.gif")
screen.title("Snake Adventures")
screen.tracer(0)
snake = []
points = 0
score()
points_player = Turtle()
points_player.penup()

style = ("Ariel", 15, "bold")

snake_length = [3]
snake_head_1 = [0]
food_eaten = 1
snake_body(snake_length[0])
screen.update()
screen.listen()
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
food = Turtle("food.gif")
food.color("red")
food.penup()

while True:
    time.sleep(0.1)
    abxy = move_forward()
    screen.update()
    #print(f"food eaten 2 = {food_eaten}")
    if food_eaten == 1:
        food.goto(random.randrange(-13, 13)*20, random.randrange(-13, 13)*20)
        food.pendown()
        #food.dot(15, "red")
        food_eaten -= 1
        screen.update()
    food.penup()
    #print(f"Snake = {snake[0].pos()} , food = {food.pos()}")
    a = snake[0].xcor()
    b = snake[0].ycor()
    c = food.xcor()
    d = food.ycor()
    if round(a) == round(c) and round(b) == round(d):
        #food.dot(15, "black")
        points_system()
        snake_length[0] = snake_length[0] + 1
        food_1 = Turtle("body_c.gif")
        food_1.color("white")
        food_1.penup()
        food_1.goto(snake[-1].pos())
        snake.append(food_1)
        #print(f" No of snake = {snake}")
        food_eaten += 1
        #print(f"food eaten 1 = {food_eaten}")
        screen.update()
    if snake[0].pos() in abxy:
        break
    if int(round(a)) <= -300 or int(round(a)) >= 300 or int(round(b)) <= -300 or int(round(b)) >= 300:
        break
print("You lose")




















screen.exitonclick()