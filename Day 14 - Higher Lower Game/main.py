import random
from game_data import data
import art

print(art.logo)

def choice_a():
    data_a = random.choice(data)

    return data_a

def choice_b():
    data_b = random.choice(data)

    return data_b

user_answer = 0
score = 0

value_a = choice_a()
game = True
while game:

    value_b = choice_b()

    computer_answer = max(value_a['follower_count'], value_b['follower_count'])
    print(f"Compare A: {value_a['name']}, a {value_a['description']}, from {value_a['country']}")
    print(art.vs)
    print(f"Against B: {value_b['name']}, a {value_b['description']}, from {value_b['country']}")

    which = input("Who has more followers? Type 'A' or 'B': ").lower()

    if which == 'a':
        user_answer = value_a['follower_count']
    elif which == 'b':
        user_answer = value_b['follower_count']

    if user_answer == computer_answer:
        score += 1
        print(f"You're right! Current score: {score}")
        value_a = value_b

    else:
        print(f"Sorry, thats wrong. Final score: {score}")
        game = False
