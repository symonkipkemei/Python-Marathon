"""
011
Task the user to enter a number over 100 and then enter a number under
10 and tell them how many times the smaller number goes into the large
number in a user-friendly format
"""

userNum1 = int(input("Enter number over 100: "))
userNum2 = int(input("Enter number below 10: "))

into = userNum1 / userNum2

into = int(into)


print(f"{userNum2} goes into {userNum1} {into} times")

