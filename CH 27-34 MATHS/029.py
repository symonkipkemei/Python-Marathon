"""
029
Ask the user to enter an integer that is over 500. Work
out the square root of that number and display it to two
decimal places
"""

import math

integer = int(input("Enter an integer above 500: "))
ans = math.sqrt(integer)
print(round(ans, 2))