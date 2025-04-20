import random

print("Welcome to Rock, Paper, Scissors!")  # Introduction
user = input("Please choose: Rock, Paper, or Scissors? \n").capitalize()  # Capitalize input for consistency

# Correct usage of random.choice()
computer = random.choice(["Rock", "Paper", "Scissors"])

print(f"\nComputer chose: {computer}")

# Game logic
if user == computer:
    print("It's a tie!")
elif (user == "Rock" and computer == "Scissors") or \
     (user == "Paper" and computer == "Rock") or \
     (user == "Scissors" and computer == "Paper"):
    print("You won! 🎉")
elif user in ["Rock", "Paper", "Scissors"]:
    print("You lost! 😢")
else:
    print("Invalid input! Please choose Rock, Paper, or Scissors.")