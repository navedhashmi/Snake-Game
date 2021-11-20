from turtle import Turtle


class Snake:

    def __init__(self):
        self.segments = []
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in self.starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        viper = Turtle("square")
        viper.color("white")
        viper.penup()
        viper.goto(position)
        self.segments.append(viper)

    def reset(self):
        for seg in self.segments:
            seg.goto(x=1000, y=1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]

    def extend(self):
        self.add_segment(self.segments[-1])

    def move(self):
        for x in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[x - 1].xcor()
            new_y = self.segments[x - 1].ycor()
            self.segments[x].goto(new_x, new_y)
        self.segments[0].fd(20)
        #if self.segments[0].xcor() == 300: # For no wall game open this code
            #tele_y = self.segments[0].ycor()
            #self.segments[0].goto(-300, tele_y)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

