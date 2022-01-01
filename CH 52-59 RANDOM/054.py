"""
054
Randomly choose either heads or tails (“h” or “t”). Ask
the user to make their choice. If their choice is the same
as the randomly selected value, display the message
“You win”, otherwise display “Bad luck”. At the end, tell
the user if the computer selected heads or tails.
"""
import random

choice = ["h", "t"]

userChoice = str.lower(input("Make your choice (h)ead or (t)ail: "))
computerSelection = random.choice(choice)
if userChoice == computerSelection:
    print("you win")
else:
    print("Bad luck")

print(f"The computer selected {computerSelection}")
