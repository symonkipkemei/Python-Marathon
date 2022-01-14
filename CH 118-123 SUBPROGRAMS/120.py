"""
120
Display the following menu to the user:
If they enter a 1, it should run a subprogram that will
generate two random numbers between 5 and 20, and
ask the user to add them together. Work out the correct
answer and return both the user’s answer and the
correct answer.
If they entered 2 as their selection on the menu, it
should run a subprogram that will generate one number
between 25 and 50 and another number between 1 and
25 and ask them to work out num1 minus num2. This
way they will not have to worry about negative answers.
Return both the user’s answer and the correct answer.
Create another subprogram that will check if the user’s
answer matches the actual answer. If it does, display
“Correct”, otherwise display a message that will say
“Incorrect, the answer is” and display the real answer.
If they do not select a relevant option on the first menu
you should display a suitable message.
"""


# GO-GETTER

# SELF EXECUTION
# The parameters are derived from the sub-program itself

def addition():
    """work out the addition from random numbers"""
    import random
    num1 = random.randint(1, 10)
    num2 = random.randint(10, 20)

    print(f"{num1} + {num2} = ")
    userAns = int(input("Answer: "))
    correctAns = num1 + num2
    ans = (userAns, correctAns)
    return ans


def subtraction():
    """ work out the subtraction from random numbers"""
    import random
    num1 = random.randint(25, 50)
    num2 = random.randint(1, 25)
    print(f"{num1} - {num2} = ")
    userAns = int(input("Answer: "))
    correctAns = num1 - num2
    ans = (userAns, correctAns)
    return ans


# EXECUTION

def check_ans(userAns, correctAns):
    """check if answer given by user is correct"""
    if userAns == correctAns:
        print("correct")
    else:
        print(f"incorrect,The answer is {correctAns}")


def main():
    """ backbone of the project"""

    print("(1) Addition\n(2) Subtraction")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        userAns, correctAns = addition()
        check_ans(userAns, correctAns)

    elif choice == 2:
        userAns, correctAns = subtraction()
        check_ans(userAns, correctAns)

    else:
        print("Incorrect input option")


main()
