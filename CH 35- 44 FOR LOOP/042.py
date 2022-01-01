"""
042
Set a variable called total to 0. Ask the user to enter
five numbers and after each input ask them if they
want that number included. If they do, then add the
number to the total. If they do not want it included,
don’t add it to the total. After they have entered all five
numbers, display the total.
"""

total = 0


for x in range(0,5):
    num = int(input("Insert a number: "))
    quiz = str.lower(input("do you want that number included (yes/no): "))
    if quiz == "yes":
        total += num
    elif quiz == "no":
        total = total
    else:
        print("wrong input,I will move to the nes number")
        total =total
print(total)
