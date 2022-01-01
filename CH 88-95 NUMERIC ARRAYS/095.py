"""
095
Create an array of five numbers
between 10 and 100 which each have
two decimal places. Ask the user to
enter a whole number between 2 and 5.
If they enter something outside of that
range, display a suitable error message
and ask them to try again until they
enter a valid amount. Divide each of the
numbers in the array by the number the
user entered and display the answers
shown to two decimal places.
"""


import array as ary
ary1 = ary.array("f", [17.98, 12.54, 11.77, 15.76, 18.32])


num = int(input("Enter a whole number between 2 and 5:"))

while num <= 2 or num >= 5:
    print("The number is out of the stated range")
    num = int(input("Try again:"))


for x in ary1:
    ans = x / num
    print(round(ans, 2))







