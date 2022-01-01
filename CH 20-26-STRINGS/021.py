""""
021
Ask the user to enter their first name and then ask them to
enter their surname. Join them together with a space between
and display the name and the length of whole name.

"""
firstName = input("Enter your first name: ")
secondName = input("Enter your second name: ")

fullName = firstName + " " + secondName

print(fullName)
print(len(fullName))