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

game = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n "))
if 0 <= choice <= 2:
    print(f"You chose:{game[choice]}")
pick = random.randint(0,2)
print(f"Computer chooses:{game[pick]}")

if 0 < choice >= 3:
    print("Nah fam you lose, buddy")
elif choice == pick:
    print("Its a tie")
elif choice == 0 and pick == 1:
    print("You lose")
elif choice == 0 and pick == 2:
    print("You win")
elif choice == 1 and pick == 0:
    print("You win")
elif choice == 1 and pick == 2:
    print("You lose")
elif choice == 2 and pick == 0:
    print("You lose")
elif choice == 2 and pick == 1:
    print("You win")