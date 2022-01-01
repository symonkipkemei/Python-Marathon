"""
059
Display five colours and ask the user to pick one. If they
pick the same as the program has chosen, say “Well
done”, otherwise display a witty answer which involves
the correct colour, e.g. “I bet you are GREEN with envy”
or “You are probably feeling BLUE right now”. Ask
them to guess again; if they have still not got it right,
keep giving them the same clue and ask the user to
enter a colour until they guess it correctly
"""

import random
colors = ["Red", "Green", "Orange", "Yellow", "White"]

print("Pick one of the colors below:")

for index, x in enumerate(colors):
    print(f"{index}. {x}")

userSelection = int(input("choose one color: "))
compChoice = random.choice(colors)

correct = True
while correct:
    if colors[userSelection] == compChoice:
        print("Well done")
        correct = False
    else:
        print(f"I bet you are {compChoice} with envy")
        userSelection = int(input("try again: "))








