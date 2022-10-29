import random
from os import system

from art import logo, vs
from data import data


def format_data(account):
    """returns the format data"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]

    return f"account {account_name}, a {account_description}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """checks and returns who have the highest follower"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
end_game = False
account_b = random.choice(data)

while not end_game:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(user_guess, a_follower_count, b_follower_count)

    system("cls")
    print(logo)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        end_game = True
        print(f"Sorry, that's wrong. Final score: {score}.")
