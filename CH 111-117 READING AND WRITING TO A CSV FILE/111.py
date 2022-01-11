"""
Create a .csv file that will store the following data. Call it “Books.csv”
"""
import csv



file = open("Books.csv", "w")
for d in range(0, 5):
    book = input("insert the name of the book: ")
    author = input("insert the author of the book:")
    yearReleased = input("insert the year the book was released: ")
    record = str(book + "," + author + "," + yearReleased + "\n")
    file.write(record)

file.close()

