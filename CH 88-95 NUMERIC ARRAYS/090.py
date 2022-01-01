"""
090
Ask the user to enter numbers. If they enter a
number between 10 and 20, save it in the array,
otherwise display the message “Outside the
range”. Once five numbers have been
successfully added, display the message “Thank
you” and display the array with each item shown
on a separate line
"""


import array as ary

num = ary.array("i", [])
correct = True
for x in range(0, 5):
    userNum = int(input("Enter a number: "))
    while userNum >= 20 or userNum <= 10:
        print("Outside the range")
        userNum = int(input("Try again: "))

    else:
        num.append(userNum)

print("Thank you")

for y in num:
    print(y)