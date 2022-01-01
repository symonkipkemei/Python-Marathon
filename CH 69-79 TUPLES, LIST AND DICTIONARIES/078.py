"""
078
Create a list containing the titles of
four TV programmes and display
them on separate lines. Ask the
user to enter another show and a
position they want it inserted into
the list. Display the list again,
showing all five TV programmes in
their new positions.
"""


programmes = ["vioja", "vituko", "karate", "tahidi", "Zora"]

for y in programmes:
    print(y)

show = input("Enter another show: ")
position = int(input("Enter the position you would like: "))

programmes.insert(position, show)


for y in programmes:
    print(y)
