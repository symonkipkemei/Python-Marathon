"""
081
Ask the user to type in their favourite school subject.
Display it with “-” after each letter, e.g. S-p-a-n-i-s-h-.
"""

schoolSubject = input("Enter your favorite school subject: ")

for x in schoolSubject:
    print(x, end="-")