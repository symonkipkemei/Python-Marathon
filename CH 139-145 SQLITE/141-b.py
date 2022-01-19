import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute(""" SELECT * FROM Books """)
for x in cursor.fetchall():
    print(x)

# Change title of book

identity = int(input("\nInsert id of book to be changed:"))

correct = True
while correct:
    print("Choose what you want to change:\n"
          "1). Title\n"
          "2). Author\n"
          "3). Date of publish\n"
          "4}. End")
    selection = int(input("choice: "))

    if selection == 1:
        title = input("Insert title of book:")
        cursor.execute("UPDATE Books SET Title =? WHERE ID=? ", [title, identity])
        db.commit()

    elif selection == 2:
        author = input("Insert Author of book:")
        cursor.execute("UPDATE Books SET Author =? WHERE ID=? ", [author, identity])
        db.commit()

    elif selection == 3:
        dateOfPublish = input("Insert date of publishing:")
        cursor.execute("UPDATE Books SET DatePublished =? WHERE ID=? ", [dateOfPublish, identity])
        db.commit()

    elif selection == 4:
        correct = False

    else:
        print("Wrong input, Try again")

cursor.execute(""" SELECT * FROM Books """)
for x in cursor.fetchall():
    print(x)
