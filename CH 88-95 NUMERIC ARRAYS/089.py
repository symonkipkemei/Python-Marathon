"""
089
Create an array which will store a list of integers.
Generate five random numbers and store them in
the array. Display the array (showing each item on
a separate line)
"""
import array as ary
import random as rd

num = ary.array("i", [])
for x in range(0, 5):
    userNum = rd.randint(10, 100)
    num.append(userNum)

for x in num:
    print(x)
