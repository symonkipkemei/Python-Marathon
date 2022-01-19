"""
Create an SQL database called PhoneBook that
contains a table called Names with the following data
"""

import sqlite3

db = sqlite3.connect("Girlfriends.db")
cursor = db.cursor()

# create a table
cursor.execute(""" CREATE TABLE IF NOT EXISTS madame(ID integer PRIMARY KEY,
name text NOT NULL,
Age integer NOT NULL,
color text );""")

# insert into a table 5 girls data
"""
for x in range(0, 5):
    name = input("Hey girl, enter your name:")
    age = int(input("Don't know you don't like mentioning your age, just let me know:"))
    color = input("Light skin or dark skin: ")
    cursor.execute("""# INSERT INTO madame(name, Age, color) VALUES(?,?,?)""", (name, age, color))
    #db.commit()


# view database
cursor.execute("""SELECT * FROM madame""")
print(cursor.fetchall())

