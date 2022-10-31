from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """All the methods related to player are in this class."""

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def move_up(self):
        """move the turtle up."""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """move the turtle to the starting position."""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """return 'true' if turtle at finish line otherwise 'false'."""
        return self.ycor() > FINISH_LINE_Y
