import time
from turtle import Turtle,Screen
from Snake import Snakes,positions
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

scores = Score()
snake = Snakes()
f = Food()
screen.listen()
screen.onkey(snake.Up,'Up')
screen.onkey(snake.Down,'Down')
screen.onkey(snake.Left,'Left')
screen.onkey(snake.Right,'Right')


on= True
pos = -60
while on:
    screen.update()
    time.sleep(.1)
    snake.move()
    if snake.head.distance(f)<15:
        f.refresh()
        snake.extent()
        scores.inc()

        # positions.clear()
        # positions.append((pos,0))
        # snake.create_snake()
        # pos-=20


    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290 or snake.head.ycor()>290:
        scores.reset()
        snake.reset()

    for tur in snake.turtles[1:]:
        if tur == snake.head:
            pass
        if snake.head.distance(tur)<10:
            scores.reset()
            snake.reset()

screen.exitonclick()

# p = [2,3,4,5,6,7,7,8,9,9,9,34,4,6,7,4]
# ap = (2,3,4,5,6,7,7,8,9,9,9,34,4,6,7,4)
#
# print(p[::-1])
# print(p[1:10:2])
# print(ap[1:10:2])
# print(p[8:11])