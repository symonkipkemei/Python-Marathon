"""
113
Using the Books.csv file, ask the user how many records
they want to add to the list and then allow them to add
that many. After all the data has been added, ask for an
author and display all the books in the list by that author.
If there are no books by that author in the list, display a
suitable message.
"""

import csv
file = open("Books.csv", "a")
userRecords = int(input("how many records do you want to add:"))
for d in range(0, userRecords):
    book = input("insert the name of the book: ")
    author = input("insert the author of the book:")
    yearReleased = input("insert the year the book was released: ")
    record = str(book + "," + author + "," + yearReleased + "\n")
    file.write(record)
file.close()

# display all the books
file = open("Books.csv", "r")
for row in file:
    print(row)
file.close()




file = open("Books.csv", "r")

#ask for an author
author = input("insert the name of the author :")
reader = csv.reader(file)
listyangu = list(reader)
print(reader)
for r in reader:
    print(r)
 kl,m 