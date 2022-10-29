from turtle import Turtle, Screen


def move_forward():
    """turtle will move forward by 10 pixels."""
    tom.forward(10)


def move_backward():
    """turtle will move backward by 10 pixels."""
    tom.back(10)


def clockwise():
    """turtle will turn right 10 pixels with respect to current heading"""
    tom.setheading(tom.heading() + 10)


def counter_clockwise():
    """turtle will turn left 10 pixels with respect to current heading"""
    tom.setheading(tom.heading() - 10)


def clear():
    """Clears the screen and returns the turtle to initial position."""
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


tom = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
