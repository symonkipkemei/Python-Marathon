"""
097
Using the 2D list from program 096, ask the user to
select a row and a column and display that value.
"""

myList = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

print(myList)


userRow = int(input("Select row: "))
userColumn = int(input("Select column: "))

print(myList[userRow][userColumn])