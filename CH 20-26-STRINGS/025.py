"""
025
Ask the user to enter their first name. If the length
of their first name is under five characters, ask
them to enter their surname and join them
together (without a space) and display the name
in upper case. If the length of the first name is five
or more characters, display their first name in
lower case
"""

name = input("enter your firstname: ")

if len(name) < 5:
    surname = input("Enter your surname: ")
    joinedName = name+surname
    print(str.upper(joinedName))

else:
    print(str.lower(name))