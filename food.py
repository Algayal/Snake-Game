"""Initialize Food component, shown in blue."""

import random
from turtle import Turtle


class Food(Turtle):
    """Creating the snake food and refreshing it when eaten."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed(0)
        self.refresh_food()

    def refresh_food(self):
        """Refreshing the food component to a random location"""
        random_x = random.randint(-265, 265)
        random_y = random.randint(-265, 265)
        self.goto(random_x, random_y)
