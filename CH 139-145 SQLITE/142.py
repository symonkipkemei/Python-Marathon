"""
Using the BookInfo database from
program 141, display the list of
authors and their place of birth. Ask
the user to enter a place of birth and
then show the title, date published
and author’s name for all the books
by authors who were born in the
location they selected.


"""
# CONNECT TO DATABASE
import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute(" SELECT * FROM Authors ")
for x in cursor.fetchall():
    print(x)

placeOfBirth = input("insert place of birth: \n")

cursor.execute("""SELECT Books.Title , Books.DatePublished, Books.Author FROM Books,Authors
WHERE Books.Author = Authors.Name  """)
for row in cursor.fetchall():
    print(row)


