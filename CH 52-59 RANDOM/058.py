"""
058
Make a maths quiz that asks five questions by randomly
generating two whole numbers to make the question
(e.g. [num1] + [num2]). Ask the user to enter the
answer. If they get it right add a point to their score. At
the end of the quiz, tell them how many they got correct
out of five.
"""

import random

print("Welcome to Lelgo's computer")
userName = str.title(input("What is your name?: "))

print(f"\nHello {userName} ,Welcome to my Maths class\n"
      f"You are going to attempt five questions.\n"
      f"If you get all of them correctly you will get Lelgo's phone and play a racing game!")

count = 0
numQuiz = 5
for x in range(0, numQuiz):
    num1 = random.randint(10, 20)
    num2 = random.randint(10, 30)
    correct = True
    while correct:
        quiz1Ans = num1 + num2
        print(f"{num1} + {num2} = ")
        userAns = int(input("answer : "))

        if userAns == quiz1Ans:
            count += 1
            correct = False

        else:
            print(f"That's wrong {userName}. Try again")
            correct = True


if count == 5:
    print(f"\nCongratulations! {userName}\n"
          f"You got {count} out of {numQuiz}\n"
          f"You can go ahead and play the racing game!")

else:
    print(f"You got {count} out of 5\n"
          f"Try next time!")








