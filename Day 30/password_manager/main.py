import random
import pyperclip
import json
import tkinter as tk
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generates random password."""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    password = []
    [password.append(random.choice(letters)) for _ in range(random.randint(8, 10))]
    [password.append(random.choice(symbols)) for _ in range(random.randint(2, 4))]
    [password.append(random.choice(numbers)) for _ in range(random.randint(2, 4))]

    random.shuffle(password)
    random_password = ''.join(password)

    password_input.delete(0, tk.END)
    password_input.insert(0, random_password)
    pyperclip.copy(random_password)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    """Searches saved account details."""
    website = website_input.get().capitalize()
    try:
        with open("passwords.txt", "r") as file:
            password_dict = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in password_dict:
            email = password_dict[website]["email"]
            password = password_dict[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website}!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    """Adds account details to a file."""
    website = website_input.get().capitalize()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave any fields empty!")
        return
    else:
        try:
            with open("passwords.txt", "r") as file:
                # Reading old data.
                data = json.load(file)
        except FileNotFoundError:
            with open("passwords.txt", "w") as file:
                # Write new data.
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data.
            data.update(new_data)

            with open("passwords.txt", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, tk.END)
            password_input.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)
website_label.focus()
email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_input = tk.Entry(width=42)
website_input.grid(row=1, column=1, columnspan=2)
email_input = tk.Entry(width=42)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(tk.END, "jagadeesh***********@gmail.com")
password_input = tk.Entry(width=24)
password_input.grid(row=3, column=1)

# Buttons
generate_password_button = tk.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = tk.Button(text="Add", width=36, command=add)
add_button.grid(row=4, column=1, columnspan=2)
search_button = tk.Button(text="Search", command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
