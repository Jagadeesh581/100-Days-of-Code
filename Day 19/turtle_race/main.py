from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=800, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

for index in range(6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[index])
    turtle.penup()
    turtle.goto(x=-380, y=y_positions[index])
    all_turtles.append(turtle)

if user_bet:
    is_game_on = True


while is_game_on:

    for turtle in all_turtles:
        if turtle.xcor() > 380:
            is_game_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner!")
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
