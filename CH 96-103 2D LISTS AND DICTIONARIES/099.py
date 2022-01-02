"""
099
Change your previous program
to ask the user which row they
want displayed. Display that
row. Ask which column in that
row they want displayed and
display the value that is held
there. Ask the user if they want
to change the value. If they do,
ask for a new value and change
the data. Finally, display the
whole row again.
"""

myList = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

print(myList)


userRow = int(input("Select row you want displayed: "))
print(myList[userRow])


userColumn = int(input("Which column in that row would you like displayed?: "))
print(myList[userRow][userColumn])

userChange = input("Would you like to change the value?(y/n): ")

if userChange == "y":
    newValue = int(input("New value: "))
    myList[userRow][userColumn] = newValue

print(myList)