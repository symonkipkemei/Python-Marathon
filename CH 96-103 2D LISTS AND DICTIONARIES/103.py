"""
103
Adapt program 102
to display the
names and ages of
all the people in
the list but do not
show their shoe
size.
"""


bata = {}
for x in range(0, 4):
    print(f"person {x +1}\n")
    name = input("name: ")
    age = int(input("age: "))
    shoeSize = int(input("shoe size: "))
    bata[name] = {"Age": age, "Shoe-size": shoeSize}


for x in bata:
    print(x)


