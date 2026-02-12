import random

choices = ["stone", "paper", "scissor"]

user = input("Enter stone, paper, or scissor: ").lower()

computer = random.choice(choices)

print("Computer chose:", computer)

if user == computer:
    print("It's a tie!")

elif user == "stone" and computer == "scissor":
    print("You win!")

elif user == "paper" and computer == "stone":
    print("You win!")

elif user == "scissor" and computer == "paper":
    print("You win!")

elif user in choices:
    print("You lose!")

else:
    print("Invalid input!")
