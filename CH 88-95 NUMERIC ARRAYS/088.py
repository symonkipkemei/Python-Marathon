""""
088
Ask the user for a list of five
integers. Store them in an array.
Sort the list and display it in
reverse order

"""

import array as ary

num = ary.array("i", [])
for x in range(0, 5):
    userNum = int(input("Insert a number: "))
    num.append(userNum)


num = sorted(num)
num.reverse()
print(num)