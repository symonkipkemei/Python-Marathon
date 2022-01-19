"""
Create a new SQL database called BookInfo that will
store a list of authors and the books they wrote.
It will have two tables. The first one should be called
Authors and contain the following data:

The second should be called Books and contain the
following data:

"""

import sqlite3

# CONNECT TO A DATABASE

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

# CREATE TABLE Authors  of 4 items
cursor.execute(""" CREATE TABLE IF NOT EXISTS Authors(
    Name text PRIMARY KEY,
    PlaceOfBirth text NOT NULL); """)

print("Fill in the following database with the mentioned Authgors\n")
for x in range(0, 4):
    name = input("Insert name:")
    placeOfBirth = input("Insert place of Birth: ")
    cursor.execute("""INSERT INTO Authors(Name,PlaceOfBirth) VALUES(?,?) """, (name, placeOfBirth))
    db.commit()

# CREATE TABLE Books  of 12 items
cursor.execute("""CREATE TABLE IF NOT EXISTS Books(
ID integer PRIMARY KEY,
Title text NOT NULL,
Author text NOT NULL,
DatePublished text NOT NULL);""")

# INSERT ITEMS TO THE Authors TABLE

print("Fill in the following database with the mentioned books\n")
for x in range(0, 12):
    # PARAMETERS
    identity = x + 1  # ID
    title = input("insert book title: ")
    author = input("insert author: ")
    datePublished = input("insert date published: ")

    cursor.execute("""INSERT INTO Books(ID,Title,Author,DatePublished) VALUES(?,?,?,?) """,
                   (identity, title, author, datePublished))
    db.commit()


