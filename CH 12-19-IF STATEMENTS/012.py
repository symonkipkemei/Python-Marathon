"""
012
Ask for two numbers. If
the first one is larger
than the second, display
the second number first
and then the first
number, otherwise show
the first number first and
then the second.
"""

num1 = int(input("Insert the first number: "))
num2 = int(input("Insert the second number: "))


if num1 > num2:
    print(num2, num1)
else:
    print(num1,num2)
