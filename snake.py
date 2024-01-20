"""Module for creating the snake player and its settings."""
from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Creating the snake, controlling it's length and movements."""

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creating the snake."""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """creating a new segment to extend the length."""
        new_square = Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.segments.append(new_square)

    def extend_length(self):
        """Extending the length by adding new segment."""
        self.add_segment(self.segments[-1].position())

    def up(self):
        """Defining the up direction."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Defining the down direction."""

        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """Defining the right direction."""

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        """Defining the left direction."""

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move(self):
        """Defining the movement where each segment
        occupies the position of the segment in front of it.
        Only the position of the head of the snake is therefore adjusted."""
        for number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[number - 1].xcor()
            new_y = self.segments[number - 1].ycor()
            self.segments[number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset_snake(self):
        """Creating a new snake in case the player lost."""
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
