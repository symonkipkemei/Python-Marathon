"""
Using the PhoneBook
database from program 139,
write a program that will
display the following menu.
If the user selects 1, they
should be able to view the
entire phonebook. If they
select 2, it should allow them
to add a new person to the
phonebook. If they select 3, it
should ask them for a
surname and then display
only the records of people
with the same surname. If
they select 4, it should ask
for an ID and then delete that
record from the table. If they
select 5, it should end the
program. Finally, it should
display a suitable message if
they enter an incorrect
selection from the menu.
They should return to the
menu after each action, until
they select 5.
"""

import sqlite3


def read():
    """viewing all items on database"""
    db = sqlite3.connect("PhoneBook1.db")
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM Names""")
    for row in cursor.fetchall():
        print(row)


def add_to_phonebook():
    """ Adding to the phonebook"""
    db = sqlite3.connect("PhoneBook1.db")
    cursor = db.cursor()
    count = 0
    cursor.execute("""SELECT * FROM Names""")
    for x in cursor.fetchall():
        count += 1
    ID = count + 1
    firstName = input("insert your first Name: ")
    surname = input("Insert your surname: ")
    phoneNumber = int(input("Insert your phoneNumber: "))

    cursor.execute(""" INSERT INTO Names(ID,FirstName,Surname,PhoneNumber) VALUES (?,?,?,?)""",
                   (ID, firstName, surname, phoneNumber))
    db.commit()
    db.close()


def read_surname():
    """ Read selected surname"""
    db = sqlite3.connect("PhoneBook1.db")
    cursor = db.cursor()

    surname = input("Insert surname:")
    cursor.execute(""" SELECT * FROM Names WHERE Surname =? """, [surname])
    for x in cursor.fetchall():
        print(x)


def delete():
    """ Delete selected item when id is inserted"""
    db = sqlite3.connect("PhoneBook1.db")
    cursor = db.cursor()
    ID = input("enter ID:")
    cursor.execute(""" DELETE FROM Names WHERE ID=?""", [ID])
    db.commit()



def main():
    """backbone"""
    correct = True
    while correct:
        print("\n Main Menu\n"
              "1) View Phone book\n"
              "2) Add to phonebook\n"
              "3) Search for surname\n"
              "4) Delete person from phonebook\n"
              "5) Quit\n")

        selection = int(input("Enter your selection: "))

        if selection == 1:
            read()

        elif selection == 2:
            add_to_phonebook()

        elif selection == 3:
            read_surname()

        elif selection == 4:
            delete()

        elif selection == 5:
            correct = False
        else:
            print("Incorrect input, Try again")


main()
