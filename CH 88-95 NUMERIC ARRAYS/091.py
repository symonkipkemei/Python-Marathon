"""
091
Create an array which contains
five numbers (two of which
should be repeated). Display
the whole array to the user. Ask
the user to enter one of the
numbers from the array and
then display a message saying
how many times that number
appears in the list.
"""

import array as ary

num = ary.array("i", [23, 25, 28, 27, 25])
print(num)

userNum = int(input("Insert a number from the array above: "))

count = num.count(userNum)

print(f"{userNum} appears {count} times in the list")
