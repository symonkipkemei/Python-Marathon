"""
034
Display the following message:
if the user enters 1, then it should ask them for
the length of one of its sides and display the
area. If they select 2, it should ask for the base
and height of the triangle and display the area. I
hey type in anything else, it should give them a
suitable error message
"""
print("Please choose one of the options below")
print("(1). Square\n"
      "(2). Triangle")
num = int(input("Enter a number: "))

if num == 1:
    sides = int(input("What is the length of one of the sides: "))
    area = sides * sides
    print(f"{area} square meters")
elif num == 2:
    base = int(input("What is the base of the triangle: "))
    height = int(input("What is the height of the triangle: "))

    areaTraingle = 0.5 * base * height
    print(f"{areaTraingle} square meters")
else:
    print("Wrong input, please go back to kindergarten!")

