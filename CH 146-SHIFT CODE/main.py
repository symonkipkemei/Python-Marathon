from sub_programs import *


def main():
    """ The backbone"""
    global gear, codeWord
    print("\nWelcome to SHIFT CODE!\n"
          "Do you want to keep a secret?\nYour crush,your fears, your insecurities\n"
          "or anything else! I will help you\n")
    correct = True
    while correct:
        print("\n1). Make a code\n"
              "2). Decode a message\n"
              "3). Quit\n")

        selection = int(input("Enter your selection: "))
        alphabet = alphabet_data()

        if selection == 1:
            codeWord = user_Word()
            gear = shift()
            coder(codeWord, gear, alphabet)

        elif selection == 2:
            codedWord = coder(codeWord, gear, alphabet)
            decoder(codedWord, gear, alphabet)

        elif selection == 3:
            correct = False
        else:
            print("Wrong input.Try again.")


main()
