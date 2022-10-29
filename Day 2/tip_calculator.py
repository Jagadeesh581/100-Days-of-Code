print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
no_of_split = int(input("How many people to split the bill? "))

pay = (total_bill + (total_bill * tip_percentage / 100)) / no_of_split

print(f"Each person should pay: ${pay:.2f}")
