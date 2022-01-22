from sub_programs import *


def main():
    myList = listColors()
    compcolors = compColors(myList)
    attempts = 0
    correct_position = 0

    print("\nThe computer has selected 4 colors already\n"
          "Let's see if you can guess them correctly\n"
          "all the best!")

    while correct_position != 4:
        usercolors_new = userColors(myList)
        correct_position = checker(compcolors, usercolors_new)
        attempts += 1

    if attempts > 10:
        print(f"Bro, You have attempted {attempts} times.\n"
              f"you need to go to kindergarten, you too slow ")

    elif attempts < 5:
        print(f"Bro, You have attempted {attempts} times.\n"
              f"you seem to have luck and charm up your sleeves! ")

    else:
        print(f"Bro, You have attempted {attempts} times.\n"
              f"This is great! You have some supper potential! ")


main()

