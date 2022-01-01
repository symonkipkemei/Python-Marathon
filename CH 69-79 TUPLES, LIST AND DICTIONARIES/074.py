"""
074
Enter a list of ten colours.
Ask the user for a starting
number between 0 and 4
and an end number
between 5 and 9. Display
the list for those colours
between the start and end
numbers the user input.
"""

colors = ["Red", "Blue", "yellow", "Green", "purple", "Brown", "White", "Orange", "Black", "Grey" ]
startNum = int(input("Enter starting number between 0 and 4: "))
endNum = int(input("Enter Ending number 5 and 9: "))

print(colors[startNum: endNum])

