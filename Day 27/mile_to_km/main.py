import tkinter as tk


# Convert miles to kms.
def on_calculate_button():
    """This Function converts miles to kms and display on kms_output label."""
    kms = round(float(miles_input.get()) * 1.609344, 2)
    kms_output.config(text=kms)


# Create a window.
window = tk.Tk()
window.title("Miles to Kilometers")
window.config(padx=40, pady=40)

# Create an Entry to take input.
miles_input = tk.Entry()
miles_input.grid(column=1, row=0)

# 'Miles' Label.
miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

# 'is equals to' Label.
equal_label = tk.Label(text="is equals to")
equal_label.grid(column=0, row=1)

# Label to display km, initially '0'.
kms_output = tk.Label(text="0")
kms_output.grid(column=1, row=1)

# 'Km' Label
kms_label = tk.Label(text="Km")
kms_label.grid(column=2, row=1)

# Button to convert miles to kms.
calculate_button = tk.Button(text="Calculate", command=on_calculate_button)
calculate_button.grid(column=1, row=2)

window.mainloop()
