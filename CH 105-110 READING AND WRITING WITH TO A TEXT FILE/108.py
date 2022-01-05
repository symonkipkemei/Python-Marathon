"""
108
Open the Names.txt file. Ask the user to input
new name. Add this to the end of the file and
display the entire file.
"""

file = open("names.txt", "a")

newName = input("input new name: ")

file.write(newName)
file.close()


file = open("names.txt", "r")
print(file.read())