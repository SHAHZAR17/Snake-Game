from turtle import Turtle
positions = [(0,0),(-20,0),(-40,0)]
MOVE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snakes:
    def __init__(self):
        self.turtles=[]
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for i in positions:
            self.add_seg(i)

    def add_seg(self,i):
        me = Turtle('square')
        me.penup()
        me.color('white')
        me.goto(i)
        self.turtles.append(me)

    def reset(self):
        for tur in self.turtles:
            tur.goto(1000,1000)
        self.turtles.clear()
        self.create_snake()
        self.head=self.turtles[0]

    def extent(self):
        self.add_seg(self.turtles[-1].position())

    def move(self):
        for tur in range(len(self.turtles) - 1, 0, -1):
            x1 = self.turtles[tur - 1].xcor()
            y1 = self.turtles[tur - 1].ycor()
            self.turtles[tur].goto(x1, y1)
        self.head.forward(MOVE)

    def Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

