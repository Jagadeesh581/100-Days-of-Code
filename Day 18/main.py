from turtle import Turtle, colormode, Screen
import random

tom = Turtle()
screen = Screen()

# for i in range(3, 11):
#     turtle.color(random.choice(colors))
#     for j in range(i):
#         turtle.forward(100)
#         turtle.left(360 / i)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# colormode(255)
# directions = [0, 90, 180, 270]
# tom.pensize(15)
# tom.speed("fastest")
#
# for _ in range(200):
#     tom.color(random_color())
#     tom.forward(30)
#     tom.setheading(random.choice(directions))

colormode(255)
tom.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        tom.color(random_color())
        tom.circle(100)
        tom.setheading(tom.heading() + size_of_gap)


draw_spirograph(1)
screen.exitonclick()
