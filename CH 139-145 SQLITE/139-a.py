""""
Create an SQL database called PhoneBook that
contains a table called Names with the following data:

"""

# CREATE/CONNECT TO A DATABASE
import sqlite3

# connect to a database
db = sqlite3.connect("PhoneBook1.db")
# create a cursor object
cursor = db.cursor()

# CREATE A TABLE CALLED Names

cursor.execute(""" CREATE TABLE IF NOT EXISTS Names(
ID integer PRIMARY KEY,
FirstName text NOT NULL,
Surname text NOT NULL,
PhoneNumber integer NOT NULL);""")

# INSERT INTO TABLE

# loop 5 times to collect user inputs

for index, x in enumerate(range(0, 5)):
    # because python starts counting from 0, yet we would like to count from 1
    ID = index + 1
    print(f"userNo. {ID}")
    firstName = input("insert your first Name: ")
    surname = input("Insert your surname: ")
    phoneNumber = int(input("Insert your phoneNumber: "))
    # field/column names should be equal to those used in creating the table (copy/paste)
    cursor.execute(""" INSERT INTO Names(ID,FirstName,Surname,PhoneNumber) VALUES (?,?,?,?)""",
                   (ID, firstName, surname, phoneNumber))
    db.commit()
