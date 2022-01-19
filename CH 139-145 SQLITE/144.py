"""
144
Using the BookInfo database, ask the user for an author’s name and then save all the
books by that author to a text file, with each field separated by dashes so it looks as
follows:
Open the text file to make sure it has worked correctly.
"""


import sqlite3
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

authorName = str(input("insert the author's name:"))


cursor.execute("""SELECT Books.ID, Books.Title, Books.Author, Books.DatePublished FROM Books
WHERE Author = ?  """, [authorName])
for row in cursor.fetchall():
    items = list(row)
    data = str(items[0]) + "-" + items[1] + "-" + items[2] + "-" + items[3] + "\n"


    # use append mode so that everytime it loops it does not override the original file
    with open("Books.txt", "a") as file:
        file.write(data)

