# 1. Go getter (RandomColors)

def listColors():
    """define a list of colors"""
    listOfColors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    return listOfColors


def compColors(colorList):
    """ Generate 4 random colors"""
    import random

    compChoice = []
    for x in range(0, 4):
        choice = str.lower((random.choice(colorList)))
        compChoice.append(choice)

    return compChoice


def userColors(colorList):
    """Tell user to enter a list of colors from a set of choices"""
    userChoice = []
    # list all the colors
    for index, x in enumerate(colorList):
        print((index + 1), x)

    print("\nThe computer has selected 4 colors already\n"
          "Let's see if you can guess them correctly\n"
          "all the best!")

    for index, x in enumerate(range(0, 4)):
        correct = True
        while correct:
            colorSelection = str.lower(input('enter color:'))
            if colorSelection in colorList:
                userChoice.append(colorSelection)
                correct = False
                print(f"color {(index + 1)}. {colorSelection} entered")
            else:
                print("Wrong spelling, try again.")

    return userChoice


def checker(compchoice, userchoice):
    """ check if the list the computer choice is ordered
     the same way by the user and award marks"""

    # colors they got right
    correct = 0
    # loop through user selected colors
    for x in userchoice:
        # loop through computer colors
        for z in compchoice:
            # if use color is equal to comp choice
            if x == z:
                correct = correct + 1

    # colours they got right in the correct position
    correct_position = 0
    # loop through comp choice
    for index, color in enumerate(compchoice):
        # check if user choice colors is same as comp choice
        if userchoice[index] == color:
            correct_position += 1

    # #colours they got right in the wrong position
    wrong_position = correct - correct_position

    print(f"You got {correct_position} in correct position\n"
          f"and {wrong_position} correct in wrong position")
    return correct_position



