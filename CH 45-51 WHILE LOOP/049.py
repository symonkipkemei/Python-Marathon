"""
049
Create a variable called
compnum and set the value
to 50. Ask the user to enter a
number. While their guess
is not the same as the
compnum value, tell them if
their guess is too low or too
high and ask them to have
another guess. If they enter
the same value as
compnum, display the
message “Well done, you
took [count] attempts”.
"""


print("Hello\n"
      "welcome to COMPNUM!\n"
      "A guessing game\n"
      "Hope you guess right.\n"
      "All the best!")
count = 0
copNum = 50
userGuess = int(input("Guess a number: "))
count += 1

while userGuess != copNum:
    if userGuess < copNum:
        print("Too low")
    elif userGuess > copNum:
        print("Too high")
    userGuess = int(input("Please, have another guess: "))
    count += 1

print(f"Well done! It took you {count} attempts")

