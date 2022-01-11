"""
112
Using the Books.csv file
from program 111, ask
the user to enter another
record and add it to the
end of the file. Display
each row of the .csv file
on a separate line.
"""


import csv

#print("enter another record: ")
#file = open("Books.csv", "a")
#book = input("insert the name of the book: ")
#author = input("insert the author of the book:")
#yearReleased = input("insert the year the book was released: ")
#record = str(book + "," + author + "," + yearReleased + "\n")
#file.write(record)


file = open("Books.csv", "r")
for row in file:
    print(row)
file.close()