from sub_programs import *


def main():
    """Backbone"""
    print("I create and store user passwords")
    correct = True
    while correct:
        print("\n1) Create a new User ID\n"
              "2) change a password\n"
              "3) display all User IDS\n"
              "4) Quit")

        user_selection = int(input("Enter selection: "))
        # create a new user ID
        if user_selection == 1:
            user_ID = user_identification()
            password = user_password()
            add_to_csv(user_ID, password)

        # change password
        elif user_selection == 2:
            user_id_changed = change_password()
            user_password()

        # display all users
        elif user_selection == 3:
            display_csv()

        elif user_selection == 4:
            correct = False

        else:
            print("wrong input")


main()
