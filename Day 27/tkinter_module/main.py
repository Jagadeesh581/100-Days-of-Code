import tkinter as tk


# Create a new window.
window = tk.Tk()
window.minsize(width=600, height=400)
window.title("Example")

# Create a label.
label = tk.Label(text="Label Text")
# Modify single property of a label.
label["text"] = "New Label Text with single modification"
# Modify multiple properties with config.
label.config(text="New Label Text with multiple modification", font=("Arial", 12, "bold"))
label.pack()


# Function do something when button is clicked.
def on_click_button():
    print("Do Something Here")


# Create a button.
button = tk.Button(text="Click Me", command=on_click_button)
button.pack()

# Create Entry(Text Input Box).
entry = tk.Entry(width=30)
# Start with some Text.
entry.insert(tk.END, string="Initial Text.")
# Get Text in Entry
print(entry.get())
entry.pack()

# Create a Text Field.
text = tk.Text(height=5, width=30)
# Puts the cursor in text box.
text.focus()
text.insert(tk.END, "Initial Text for the Text Box.")
# Gets the current value in text box at line 1, from character 0 to end.
print(text.get("1.0", tk.END))
text.pack()


# Function to do something when the value is changes in the spinbox.
def on_spinbox():
    print(spinbox.get())


# Create a Spinbox.
spinbox = tk.Spinbox(from_=0, to=10, width=5, command=on_spinbox)
spinbox.pack()


# Function to do something with the value when scale is moved.
def on_scale(value):
    print(value)


# Create a Scale.
scale = tk.Scale(from_=0, to=100, command=on_scale)
scale.pack()


# Function to do something when the button is checked. When box is checked it will get '1' otherwise '0'.
def on_checkbutton():
    print(checked_state.get())


# Set state to int variable ie, 0 or 1.
checked_state = tk.IntVar()
# Create checkbutton.
checkbutton = tk.Checkbutton(text="Is on?", variable=checked_state, command=on_checkbutton)
checkbutton.pack()


# Function to do something when one of the option is selected.
def on_radio():
    print(radio_state.get())


radio_state = tk.IntVar()
# Create a Radiobutton.
radiobutton_1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=on_radio)
radiobutton_2 = tk.Radiobutton(text="Option1", value=2, variable=radio_state, command=on_radio)
radiobutton_1.pack()
radiobutton_2.pack()


# Function to do something when the item is selected from listbox.
def on_listbox(event):
    print(listbox.get(listbox.curselection()))


fruits = ["Apple", "Banana", "Orange", "Grapes", "Pear"]
# Create a listbox.
listbox = tk.Listbox(height=3)
# Insert items into listbox.
for fruit in fruits:
    listbox.insert(fruit.index(fruit), fruit)
# Bind the listbox to the function.
listbox.bind("<<ListboxSelect>>", on_listbox)
listbox.pack()

window.mainloop()
