from random import randint


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    """Sets Difficulty level to 'easy' or 'hard'. sets initial attempts according to difficulty user chose."""
    level = input("choose a difficulty. Type 'easy' or 'hard': ")

    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_answer(guess, answer, turns):
    """Checks the guess and answer and return remaining attempts."""
    if guess > answer:
        print("Too High.")
        return turns - 1
    elif guess < answer:
        print("Too Low.")
        return turns - 1
    elif guess == answer:
        print(f"You got it! The answer was {answer}.")


def game():
    """Game starts from here."""
    print("Welcome to the Number Guessing game!")
    print("I'm  thinking a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You run out of guesses. You lose!")
            break
        elif guess != answer:
            print("Guess again.")


if __name__ == "__main__":
    game()
