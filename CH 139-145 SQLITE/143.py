"""
143
Using the BookInfo database, ask the user to
enter a year and display all the books
published after that year, sorted by the year
they were published.

"""

import sqlite3
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

year = str(input("insert a year:"))


cursor.execute("""SELECT Books.Title FROM Books
WHERE Books.DatePublished > ?  """, [year])
for row in cursor.fetchall():
    print(row)


