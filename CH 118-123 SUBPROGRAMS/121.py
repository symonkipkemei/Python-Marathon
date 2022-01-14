"""
121
Create a program that will allow the user to easily manage a list of names. You should
display a menu that will allow them to add a name to the list, change a name in the
list, delete a name from the list or view all the names in the list. There should also be a
menu option to allow the user to end the program. If they select an option that is not
relevant, then it should display a suitable message. After they have made a selection
to either add a name, change a name, delete a name or view all the names, they
should see the menu again without having to restart the program. The program
should be made as easy to use as possible.
"""

# add a name in the list
# change name in a list
# delete name from a list
# view all the names in the list
# end program


girlFriends = ["june", "perpetual", "Sharon", "Chemist", "Diana"]


def add():
    """add another girlfriend to the list"""
    name = input("insert another girFriend: ")
    girlFriends.append(name)


def change():
    """change the value of the girlfriend"""
    for index, girl in enumerate(girlFriends):
        print(f"{index}. {girl}")
    index = int(input("insert index you want to change: "))
    value = input("insert the name of the new girlfriend:")
    girlFriends[index] = value


def deleteBae():
    """Delete babe"""
    for index, girl in enumerate(girlFriends):
        print(f"{index}. {girl}")
    index = int(input("insert index of the girlfriend you want to delete: "))
    del girlFriends[index]


def list_girls():
    """List the bevy of beauties"""
    for index, girl in enumerate(girlFriends):
        print(f"{index}. {girl}")


def main():
    correct = True
    while correct:
        print("\n(1) Add girlfriend\n"
              "(2) change name of girlfriend\n"
              "(3) delete name of girlfriend\n"
              "(4) view all the girlfriends\n"
              "(5) end\n"
              )
        selection = int(input("insert: "))

        if selection == 1:
            add()
        elif selection == 2:
            change()
        elif selection == 3:
            deleteBae()
        elif selection == 4:
            list_girls()
        elif selection == 5:
            correct = False
        else:
            print("incorrect input")


main()
