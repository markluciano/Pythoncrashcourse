#Rock, Paper, Scissors variables

import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

#Game rules: Rock beats scissors beats paper beats rock

user_action = input("Enter a choice (rock, paper, scissors): ")

possible_action = [rock, paper, scissors]
computer_action = random.choice(possible_action)

print(f"\nYou chose {user_action} and computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. Its a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose!")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose!")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose!")
