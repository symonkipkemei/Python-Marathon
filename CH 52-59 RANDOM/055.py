"""
055
Randomly choose a number between 1 and 5. Ask the user to pick a
number. If they guess correctly, display the message “Well done”,
otherwise tell them if they are too high or too low and ask them to pick a
second number. If they guess correctly on their second guess, display
Correct”, otherwise display “You lose”.
"""
import random
compChoice = random.randint(1, 5)

userNum = int(input("Guess a number: "))

if userNum == compChoice:
    print("well done")

else:
    if userNum > compChoice:
        print("too high")
    else:
        print("Too low")
    secondGuess = int(input("Guess a second number: "))

    if secondGuess == compChoice:
        print("correct")
    else:
        print("You lose")



