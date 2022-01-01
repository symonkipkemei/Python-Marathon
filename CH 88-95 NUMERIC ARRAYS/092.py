"""
092
Create two arrays (one
containing three numbers that
the user enters and one
containing a set of five random
numbers). Join these two arrays
together into one large array.
Sort this large array and display
it so that each number appears
on a separate line
"""

import  random as rd
import  array as ary


# array by random
num2 = ary.array("i", [])
for x in range(0, 5):
    userNum = rd.randint(10, 100)
    num2.append(userNum)

for x in num2:
    num2.append(x)

num1 = sorted(num1)

for x in num1:
    print(x)