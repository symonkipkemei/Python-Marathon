"""
033
Ask the user to enter two numbers.
Use whole number division to divide
the first number by the second and
also work out the remainder and
display the answer in a user-friendly
way (e.g. if they enter 7 and 2 display
“7 divided by 2 is 3 with 1
remaining”).

"""

num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))

ans = int(num1/num2)
rem = num1 % num2


print(f"{num1} divided by {num2} is {ans} with {rem} remaining.")
