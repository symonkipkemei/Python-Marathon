"""
086
Ask the user to enter a new password. Ask
them to enter it again. If the two passwords
match, display “Thank you”. If the letters are
correct but in the wrong case, display the
message “They must be in the same case”,
otherwise display the message “Incorrect”.
"""

password = input("Enter a new password: ")
password2 = input("Enter password again: ")


if password == password2:
    print("Thank you")

elif str.lower(password )== str.lower(password2):
    print("They must be in the same case")

else:
    print("Incorrect")

