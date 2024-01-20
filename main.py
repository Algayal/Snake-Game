"""The famous snake game"""
import time
from turtle import Screen

from food import Food
from scoreboard import Score
from snake import Snake

screen = Screen()

# Screen settings
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# A new object has the specs of 20*20 pixels
snake = Snake()

food = Food()
score = Score()


# Assigning functions the keyboard's keys
screen = Screen()
screen.listen()
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh_food()
        score.current_score += 1
        score.score_text()
        snake.extend_length()  # extend the tail when food is eaten

    # detect collision with wall
    if (
        snake.head.xcor() > 295
        or snake.head.xcor() < -300
        or snake.head.ycor() > 300
        or snake.head.ycor() < -290
    ):
        score.reset()
        snake.reset_snake()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset_snake()


screen.exitonclick()
