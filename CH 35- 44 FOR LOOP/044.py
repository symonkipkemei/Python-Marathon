"""
044
Ask how many people the user wants to invite to a party. If they enter a number below
10, ask for the names and after each name display “[name] has been invited”. If they
enter a number which is 10 or higher, display the message “Too many people”.
"""


guests = int(input("How many guests do you want to invite into the party?: "))

if guests < 10:
    for x in range(0,guests):
        name = str.title(input("What is the name of the guest?: "))
        print(f"{name} has been invited to the party")
else:
    print("Too many people")


