"""
101
Using program 100, ask the user for a name and a region. Display the relevant data. Ask
the user for the name and region of data they want to change and allow them to make
the alteration to the sales figure. Display the sales for all regions for the name they
choose
"""


sales = {"John": {"N": 3056, "E": 8463, "W": 8441, "S": 2694},
         "Tom": {"N": 4832, "E": 6786, "W": 4737, "S": 3612},
         "Anne": {"N": 5239, "E": 4802, "W": 5820, "S": 1859},
         "Fiona": {"N": 3904, "E": 3645, "W": 8821, "S": 2451}}

name = str.title(input("What is s your name: "))
region = str.upper(input("What is s your region: "))

print(sales[name][region])

name1 = str.title(input("What is the name you want to change: "))
region1 = str.upper(input("What is the region you want to change: "))


change = int(input("New data: "))


sales[name1][region1] = change

for y in sales[name1]:
    print(sales[name1][y])