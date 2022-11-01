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
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())

        self.update_score()

    def update_score(self):
        """updates the score and prints the score at the top of the screen."""
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        """Increases the score by 1"""
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     """Stops the game and prints 'Game Over' in the middle of the screen."""
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGN, font=FONT)

    def reset_score(self):
        """updates the high score and resets the score to 0"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_score()
