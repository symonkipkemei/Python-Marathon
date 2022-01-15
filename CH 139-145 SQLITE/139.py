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

