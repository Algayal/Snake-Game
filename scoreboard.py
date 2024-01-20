"""Create a scoreboard and update it"""
from turtle import Turtle


class Score(Turtle):
    """Scoreboard settings"""

    current_score = 0

    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.score_text()

    def score_text(self):
        """Create the scoreboard"""
        self.clear()
        self.write(
            f"Current Score: {self.current_score} High Score {self.high_score}",
            False,
            "center",
            "Arial",
        )
        self.hideturtle()

    def reset(self):
        """Reset the score to zero"""
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        self.current_score = 0
        self.score_text()
