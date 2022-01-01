"""
008
Ask for the total price of the bill, then ask how
many diners there are. Divide the total bill by the
number of diners and show how much each
person must pay.
"""

bill = int(input("What's the total price of the bill?: "))
dinners = int(input("How many dinners are there?: "))

eachPerson = bill/dinners

print(f"Each person will pay {eachPerson} dollars.")
