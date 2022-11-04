import turtle
import pandas


# Set up screen with Map image. Note: turtle package supports only .gif format.
screen = turtle.Screen()
screen.title("States Of India Game")
image = "india_map_blank.gif"
screen.addshape(image)
turtle.shape(image)


# Get the coordinates in on the screen.
# def get_mouse_click(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click)

# read csv data using pandas
states_data = pandas.read_csv("states.csv")
states_list = states_data["state"].to_list()
guessed_states = []
guessed_islands = []

# Continue until user guesses all the states and islands
while len(guessed_states) < 29 or len(guessed_islands) < 2:
    answer_text = screen.textinput(title=f"{len(guessed_states)}/29 states & {len(guessed_islands)}/2 islands correct",
                                   prompt="Enter next one:").title().strip()

    if answer_text == "Exit":
        # missing_states_and_islands = []
        # for state in states_list:
        #     if state not in guessed_states and state not in guessed_islands:
        #         missing_states_and_islands.append(state)

        # Replacing above statements with list comprehension.
        missing_states_and_islands = [state for state in states_list if state not in guessed_states
                                      and state not in guessed_islands]
        missing_data = pandas.DataFrame(missing_states_and_islands)
        missing_data.to_csv("missing_states_and_islands.csv")
        break

    if answer_text in states_list:
        turtle_1 = turtle.Turtle()
        turtle_1.hideturtle()
        turtle_1.penup()
        state_data = states_data[states_data.state == answer_text]
        turtle_1.goto(int(state_data.x), int(state_data.y))
        turtle_1.write(answer_text)

        if answer_text == "Lakshadweep" or answer_text == "Andaman And Nicobar Islands" \
                and answer_text not in guessed_islands:
            guessed_islands.append(answer_text)
        elif answer_text not in guessed_states:
            guessed_states.append(answer_text)
