"""
085
Ask the user to type in their name
and then tell them how many vowels
are in their name
"""


userName = input("Type your name: ")
count = 0
for x in userName:
    vowels = ["a", "e", "i", "o", "u"]
    if x in vowels:
        count += 1

print(f"There are {count} vowels in {userName}")