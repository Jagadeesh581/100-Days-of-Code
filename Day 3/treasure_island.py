print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

left_or_right = input("You're at a cross road, where do you want to go? Type 'left' or 'right': ").lower()

if left_or_right == "left":
    swim_or_wait = input("You've come to a lake. There is an island in the middle of the lake."
                         " Type 'wait' to wait for boat. Type 'swim' to swim across the lake: ").lower()
    if swim_or_wait == "wait":
        selected_door = input("You arrive at the island. There is a house with 3 doors. 'red', 'yellow' and 'blue'."
                              " Which color do you choose: ").lower()
        if selected_door == "red":
            print("You burned by fire. Game Over.")
        elif selected_door == "yellow":
            print("You selected the correct door. You Win!")
        elif selected_door == "blue":
            print("You eaten by beasts. Game Over.")
        else:
            print("You selected a door that does not exist. Game Over.")
else:
    print("You fell into hole. Game Over.")
