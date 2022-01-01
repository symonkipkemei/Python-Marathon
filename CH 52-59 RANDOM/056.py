"""
056
Randomly pick a whole number between 1
and 10. Ask the user to enter a number and
keep entering numbers until they enter the
number that was randomly picked.
"""

import random
ranNum = random.randint(1, 10)
userNum = int(input("Enter a number: "))
while userNum != ranNum:
    userNum = int(input("Enter a number: "))


