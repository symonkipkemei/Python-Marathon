"""
093
Ask the user to enter five
numbers. Sort them into order
and present them to the user.
Ask them to select one of the
numbers. Remove it from the
original array and save it in a
new array
"""


# import array
import array as ary
import random as rd

# array by user
num1 = ary.array("i", [])
for x in range(0, 5):
    userNum = int(input("Insert a number: "))
    num1.append(userNum)


num1 = sorted(num1)

for x in num1:
    print(x)

userSel = int(input("select one of the numbers: "))
num1.remove(userSel)


num2 = ary.array("i", [])
num2.append(userSel)

for x in num1:
    print(x)

print(num2)
