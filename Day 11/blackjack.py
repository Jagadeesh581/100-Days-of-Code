from os import system
import random

from art import logo


def deal_card():
    """returns random card from the pack of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """returns sum of cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    """checks and returns if user win or lost"""
    if user_score > 21:
        return "You went over you lose!"
    elif computer_score > 21:
        return "Computer went over, You Win"
    elif user_score == computer_score:
        return "Draw!"
    elif user_score == 0:
        return "You Win with Blackjack 😎"
    elif computer_score == 0:
        return "You Lose, Computer have a Blackjack 😥"
    elif user_score > computer_score:
        return "You Win"
    else:
        return "You Lose"


def play():
    """Game starts from this function"""
    print(logo)

    user_cards = []
    computer_cards = []
    game_over = False
    computer_score = 0
    user_score = 0

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # if user_score less than 21 ask user if he/she wants to draw another card, if input is 'y' draw another card.
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    # if the computer score is not equals to zero and less than 17 computer must draw another card.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


if __name__ == "__main__":
    # continue playing the game if user types 'y'.
    while input("Do you want to play blackjack? Type 'y' for yes: ").lower() == "y":
        system("cls")
        play()
