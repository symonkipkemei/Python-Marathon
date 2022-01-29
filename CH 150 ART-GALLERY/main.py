from sub_programs import *


def main():
    """backbone"""

    correct = True
    while correct:
        print("\nThe Art Gallery database")

        print("1) create a table\n"
              "2) insert data in the table\n"
              "3) search item \n"
              "4) Buy art\n"
              "5) Quit")

        user_selection = int(input("user selection:"))

        if user_selection == 1:
            create_tables()

        elif user_selection == 2:
            list_of_ids = check_artist_id()
            list_of_piece = check_piece_id()
            insert_table(list_of_ids,list_of_piece )
        elif user_selection == 3:
            view_table()
        elif user_selection == 4:
            sell_piece_item()
        elif user_selection == 5:
            correct = False
        else:
            print("wrong input")


main()
