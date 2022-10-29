import colorgram
import turtle
import random


colors = colorgram.extract("image.png", 38)
rgb_colors = []

tom = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
tom.penup()
tom.speed("fastest")
tom.hideturtle()

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

tom.setposition(-220, -220)
for row in range(10):
    for column in range(10):
        tom.dot(20, random.choice(rgb_colors))
        tom.forward(50)
    tom.setposition(-220, tom.ycor() + 50)

screen.exitonclick()
