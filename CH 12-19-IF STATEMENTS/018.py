"""
018
Ask the user to enter a number. If it is under 10,
display the message “Too low”, if their number is
between 10 and 20, display “Correct”, otherwise
display “Too high”.
"""

num = int(input("Insert a number: "))


if num < 10:
    print("too low")
elif 10 < num < 20:
    print("correct")
else:
    print("too high")


