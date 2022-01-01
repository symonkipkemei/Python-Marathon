"""
073
Ask the user to
enter four of their
favourite foods
and store them in
a dictionary so
that they are
indexed with
numbers starting
from 1. Display
the dictionary in
full, showing the
index number
and the item. Ask
them which they
want to get rid of
and remove it
from the list. Sort
the remaining
data and display
the dictionary
"""

food = {1: "Chapati", 2: "Meat", 3: "Fruits", 4: "Rice", 5: "Sweet potatoes"}


print(food)
deleteFood = int(input("Which of the above foods don't you like?: "))

del food[deleteFood]
print(food)
