"""
094
Display an array of five
numbers. Ask the user to
select one of the numbers
Once they have selected a
number, display the
position of that item in the
array. If they enter
something that is not in
the array, ask them to try
again until they select a
relevant item
"""


import  random as rd
import  array as ary


# array by random
num2 = ary.array("i", [])
for x in range(0, 5):
    userNum = rd.randint(10, 100)
    num2.append(userNum)

# display numbers
for z in num2:
    print(z)

# select one
userSel = int(input("select one of the numbers: "))

while userSel not in num2:
    userSel = int(input("Try again: "))

position = num2.index(userSel)

print(f"{userSel} is in position {position}")



