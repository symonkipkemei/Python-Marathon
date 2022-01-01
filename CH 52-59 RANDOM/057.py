"""
057
Update
program 056
so that it
tells the
user if they
are too high
or too low
before they
pick again.
"""

import random
ranNum = random.randint(1, 10)
userNum = int(input("Enter a number: "))
while userNum != ranNum:
    if userNum > ranNum:
        print("too high")
    else:
        print("too low")
    userNum = int(input("Enter a number: "))
