import random
from os import system

import stages

word_list = ["apple", "chrome", "python", "cake"]
random_word = random.choice(word_list)
blank_word = list("_" * len(random_word))

game_over = False
life = 6

print(stages.ascii_hangman)

while not game_over:
    user_guess = input("Guess a word: ").lower()

    system("cls")

    for index in range(len(blank_word)):
        if random_word[index] == user_guess:
            blank_word[index] = user_guess

    print(f"word: {''.join(blank_word)}")
    print(stages.stages[life - 1])
    
    if user_guess not in random_word:
        life -= 1
        print("wrong guess, you lose a life!")
    if "_" not in blank_word:
        game_over = True
        print("You win!")
    elif life == 0:
        game_over = True
        print("You lose!")
