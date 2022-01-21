from sub_programs import *


def main():
    myList = listColors()
    usercolors = userColors(myList)
    compcolors = compColors(myList)
    checker(compcolors, usercolors)


main()
