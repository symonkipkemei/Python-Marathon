"""
005
Ask the user to enter three
numbers. Add together the first
two numbers and then multiply
this total by the third. Display the
answer as The answer is
[answer].
"""

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
num3 = int(input("enter the second number: "))

# adding the first two numbers together

ans1 = num1 + num2
# multiply the answer above with num 3
ans2 = ans1 * num3

print(f"The answer is [{ans2}]")
