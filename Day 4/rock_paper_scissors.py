import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


signs = [rock, paper, scissors]
my_choice = int(input("What do you chose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
computer_choice = random.randint(0, 2)

print(signs[my_choice])
print("Computer Choose:")
print(signs[computer_choice])

# if my_choice == computer_choice:
#     print("It's a draw!")
# elif my_choice == 0:
#     if computer_choice == 2:
#         print("You win!")
#     elif computer_choice == 1:
#         print("You lose!")
# elif my_choice == 1:
#     if computer_choice == 0:
#         print("You Win!")
#     elif computer_choice == 2:
#         print("You lose!")
# elif my_choice == 2:
#     if computer_choice == 1:
#         print("You Win!")
#     elif computer_choice == 0:
#         print("You lose!")
# else:
#     print("Invalid Input.")

if my_choice == computer_choice:
    print("It's a draw!")
elif (my_choice == 0 and computer_choice == 2) or (my_choice == 1 and computer_choice == 0) or (
        my_choice == 2 and computer_choice == 1):
    print("You Win!")
elif (my_choice == 0 and computer_choice == 1) or (my_choice == 1 and computer_choice == 2) or (
        my_choice == 2 and computer_choice == 0):
    print("You Lose!")
else:
    print("Invalid Input")
