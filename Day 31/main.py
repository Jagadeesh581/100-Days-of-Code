import pandas

import os
import random
import tkinter as tk
from tkinter import messagebox

# Constants
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

current_word = {}

try:
    to_learn_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/hindi_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = to_learn_data.to_dict(orient="records")


def next_word():
    """Randomly displays a word and after calls flip_card function after 3 seconds."""
    global current_word
    current_word = random.choice(words_to_learn)
    canvas.itemconfig(canvas_img, image=front_image)
    canvas.itemconfig(title_text, text="Hindi", fill="black")
    canvas.itemconfig(word_text, text=current_word["Hindi"], fill="black")

    window.after(3000, flip_card)


def flip_card():
    """Flips the card to back side."""
    canvas.itemconfig(canvas_img, image=back_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_word["English"], fill="white")


def known():
    """Remove the words which the user already know and save the unknown words into new file."""
    words_to_learn.remove(current_word)
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()


def reset():
    """Reset the progress."""
    try:
        os.remove("data/words_to_learn.csv")
    except FileNotFoundError:
        messagebox.showinfo(title="Reset", message="You do not have any learning history.")
    else:
        messagebox.showinfo(title="Reset", message="Flash Cards reset to initial state.")


# Window
window = tk.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
front_image = tk.PhotoImage(file="./images/card_front.png")
back_image = tk.PhotoImage(file="./images/card_back.png")
right_image = tk.PhotoImage(file="./images/right.png")
wrong_image = tk.PhotoImage(file="./images/wrong.png")

# Canvas
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = canvas.create_image(400, 263, image=front_image)
title_text = canvas.create_text(400, 150, text="", font=TITLE_FONT)
word_text = canvas.create_text(400, 253, text="", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_button = tk.Button(image=right_image, highlightthickness=0, command=known)
right_button.grid(row=1, column=0)
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, command=next_word)
wrong_button.grid(row=1, column=1)
reset_button = tk.Button(text="Reset", command=reset)
reset_button.config(width=36, fg="red")
reset_button.grid(row=2, column=0, columnspan=2)

next_word()

window.mainloop()
