"""
It should save the data to an SQL database called
TestScores when the Add button is clicked. The Clear
button should clear the window.

"""

import sqlite3

# CONNECT TO A DATABASE

with sqlite3.connect("TestScores.db") as db:
    cursor = db.cursor()

# CREATE TABLE Scores
cursor.execute(""" CREATE TABLE IF NOT EXISTS Scores(
    StudentName text PRIMARY KEY,
    StudentGrade text NOT NULL); """)

# INSERT INTO database
value = int(input("How many students do you want to add: "))
for x in range(0,value):
    # parameters
    name = input("insert student name:")
    grade = input("insert student grade:")

    cursor.execute(""" INSERT INTO Scores(StudentName,StudentGrade) VALUES(?,?) """, [name, grade])
    db.commit()


cursor.execute("SELECT * FROM Scores ")
for x in cursor.fetchall():
    print(x)
