import random
from art import logo

print(logo)

def guess(level):
    tries = 0

    if level == "easy":
        tries = 10
    else:
        tries = 5

    return tries

def math(attempts):
    number = random.randint(1, 100)

    game = True
    while game:
        if attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number")
            picknum = int(input("Make a guess: "))
            attempts -= 1
            if attempts == 0:
                print("You lost the game")
                return

            if picknum != number:
                if picknum > number:
                    print("Too high.")
                    print("Guess again")
                elif picknum < number:
                    print("Too low")
                    print("Guess again")
            else:
                print(f"You got it! It was {number}!")
                game = False


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficult. Type 'easy' or 'hard': ")
goes = guess(difficulty)
math(goes)
