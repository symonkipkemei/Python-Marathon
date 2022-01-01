"""
038
Change program
037 to also ask for a
number. Display
their name (one
letter at a time on
each line) and
repeat this for the
number of times
they entered.
"""


userName = input("Enter your name: ")
num = int(input("Enter a number: "))

for x in range(0, num):
    for y in userName:
        print(y)



