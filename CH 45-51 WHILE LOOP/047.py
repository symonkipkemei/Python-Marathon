"""
047
Ask the user to enter a
number and then enter
another number. Add these
two numbers together and
then ask if they want to add
another number. If they
enter “y", ask them to enter
another number and keep
adding numbers until they
do not answer “y”. Once th
loop has stopped, display
the total.
"""
total = 0
num = int(input("Enter a number: "))

quiz = "y"
while quiz == "y":
    num = int(input("Enter another number: "))
    quiz = str.lower(input("Do you want to add another number?(y): "))
    total += num

print(total)
