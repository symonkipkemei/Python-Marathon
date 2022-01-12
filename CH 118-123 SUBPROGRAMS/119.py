"""
Define a subprogram that will ask the user to
pick a low and a high number, and then
generate a random number between those
two values and store it in a variable called
“comp_num”.

Define another subprogram that will
give the instruction “I am thinking of a number…”
and then ask the user to guess the number they
are thinking of.

Define a third subprogram that will
check to see if the comp_num is the same
as the user’s guess. If it is, it should display the
message “Correct, you win”, otherwise it should
keep looping, telling the user if they are too low or
too high and asking them to guess again until they
guess correctly.
"""


# GO-GETTER

def random_num():
    """generate a random number between a high and a low value"""
    import random
    """Random number"""
    highNum = int(input("enter a high number: "))
    lowNum = int(input("enter a low number: "))
    comp_num = random.randint(lowNum, highNum)
    return comp_num


def guess_num():
    """User to guess a number"""
    print("I am thinking of a number....")
    userGuess = int(input("Guess a number: "))
    return userGuess

def main():
    correct = True
    compNum = random_num()
    while correct:
        guessNum = guess_num()
        if guessNum == compNum:
            print("correct, you win ")
            correct = False
        else:
            if guessNum > compNum:
                print("Too high")
            else:
                print("Too low")
            correct = True


main()