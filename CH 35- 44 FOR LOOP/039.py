"""
039
Ask the user to enter a number between 1
and 12 and then display the times table for
that number.
"""

num = int(input("Enter a number between 1 and 12: "))


for x in range(0, num+1):
    print(f"{num}x{x}")

