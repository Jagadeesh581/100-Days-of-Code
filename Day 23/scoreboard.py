from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """All the scoreboard related methods are in this class."""

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears the previous score and updates the scoreboard."""
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT, align="left")

    def increase_level(self):
        """Increase the level by 1."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Write 'GAME OVER' message at the center of the screen."""
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", font=FONT, align="left")
