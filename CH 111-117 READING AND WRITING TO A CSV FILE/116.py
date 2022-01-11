"""
116
Import the data from the Books.csv file into a list. Display the
list to the user. Ask them to select which row from the list
they want to delete and remove it from the list. Ask the user
which data they want to change and allow them to change it.
Write the data back to the original .csv file, overwriting the
existing data with the amended data.
"""
# IMPORTING DATA INTO A LIST
# import csv
import csv

# open csv file
file = open("Books.csv", "r")

# convert into an iterable
reader = csv.reader(file)

# list the iterables
rows = list(reader)

# DISPLAY LIST TO THE USER
print("The following are book items within my repository")
for index, row in enumerate(rows):
    print(f"{index}. {row}")

# DELETE ROW

# abstract the index of the row to be deleted
userRow = int(input("\nwhich row do you want to delete?: "))

# delete the row
del rows[userRow]

# display the new list
print("\nThe following are the remaining book items within my repository")
for index, row in enumerate(rows):
    print(f"{index}. {row}")

# DATA CHANGE

# ask for the row they want to change and display that row
userRowChange = int(input("\nwhich row do you want to change?: "))
print(rows[userRowChange])

# ask for the column
userColumnChange = int(input("\nwhich column do you want to change?: "))

# ask the new value
value = input("Input the new value: ")

# change the value
rows[userRowChange][userColumnChange] = value

# confirm if the value has been effected

# display the new list
print("\nThis the new data list")
for index, row in enumerate(rows):
    print(f"{index}. {row}")

# OVERRIDE THE NEW CHANGES TO THE EXISTING CSV FILE

# create a temporary 2d list
# to freeze the changes made already
tmp = []

for row in rows:
    tmp.append(row)
print("\nOur new temporary list")
print(tmp)

# opening the original csv file
file = open("Books.csv", "w")
# the w option allows us to override the csv file
# break 2d list to rows

for row in tmp:
    # do you know the number of columns present
    data = str(row[0] + "," + row[1] + "," + row[2] + "\n")
    # remember to convert the variable to string
    file.write(data)

file.close()