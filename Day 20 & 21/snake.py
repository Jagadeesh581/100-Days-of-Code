from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """This class takes care of all the functionalities related to snake like creating snake,
     increasing snake length and moving the snake."""

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """create the snake."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """adds new segment to the snake."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """increases snake length."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves all the snake segments at a time, so that it will look like a single segment."""
        for index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Turn the snake direction to up if it is not heading towards downside."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turn the snake direction to down if it is not heading towards upside."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turn the snake direction to left if it is not heading towards right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turn the snake direction to right if it is not heading towards left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
