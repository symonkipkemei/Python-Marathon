# CREATE/CONNECT TO A DATABASE
import sqlite3

# connect to a database
db = sqlite3.connect("PhoneBook1.db")
# create a cursor object
cursor = db.cursor()


cursor.execute("""SELECT * FROM Names""")
for x in cursor.fetchall():
    print(x)

cursor.execute("""SELECT surname FROM Names""")
for x in cursor.fetchall():
    print(x)

cursor.execute("""SELECT surname FROM Names WHERE PhoneNumber = 0718454749""")
for x in cursor.fetchall():
    print(x)


