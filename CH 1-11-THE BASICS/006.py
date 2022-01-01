"""
006
Ask how many slices
of pizza the user
started with and ask
how many slices
they have eaten.
Work out how many
slices they have left
and display the
answer in a userfriendly format.
"""

print("Welcome to Pizzain!\n")

pizzaSlices = int(input("How many slices did you start with?: "))
eatenSlices = int(input("How many slices have you eaten?: "))

leftSlices = pizzaSlices - eatenSlices

print(f"Hello!\nYou have left the {leftSlices} slices of pizza.")
