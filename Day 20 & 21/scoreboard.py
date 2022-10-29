from turtle import Turtle


ALIGN = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    """Keeps track of the Score."""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        """updates the score and prints the score at the top of the screen."""
        self.write(f"Score:{self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        """Increases the score by 1"""
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        """Stops the game and prints 'Game Over' in the middle of the screen."""
        self.goto(0, 0)
        self.write("Game Over", align=ALIGN, font=FONT)
