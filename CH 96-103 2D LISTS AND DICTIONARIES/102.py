"""
102
Ask the user to enter the name, age and shoe size for four
people. Ask for the name of one of the people in the list and
display their age and shoe size.
"""

bata = {}
for x in range(0, 4):
    print(f"person {x +1}\n")
    name = input("name: ")
    age = int(input("age: "))
    shoeSize = int(input("shoe size: "))
    bata[name] = {"Age": age, "Shoe-size": shoeSize}


for x in bata:
    print(bata[x])


name = input("Enter the name of one person: ")


print(bata[name])

for x in bata[name]:
    print(x)

print(bata)