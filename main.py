from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

flag = True
while flag:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()

    # detect collision with wall
    wall = snake.head.xcor()
    wall2 = snake.head.ycor()
    if wall > 280 or wall < -300 or wall2 > 295 or wall2 < -280:
        scoreboard.resat()
        snake.resat()

    # detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.resat()
            snake.resat()




screen.exitonclick()
