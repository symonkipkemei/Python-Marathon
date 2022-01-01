"""
036
Alter program 035 so that it will ask the user to enter their
name and a number and then display their name that
number of times.
"""

userName = input("Enter your name: ")
num = int(input("Enter a number: "))

for x in range(0, num):
    print(userName)

