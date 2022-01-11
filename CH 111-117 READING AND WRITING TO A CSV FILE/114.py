""""
114
Using the Books.csv file, ask the user
to enter a starting year and an end
year. Display all books released
between those two years.
"""


import csv

# before we begin we have to open the file fas

file = open("Books.csv", "r")
# convert csv into an iterable
reader = csv.reader(file)

#printing

print("Hello, the following books are present in my repository: ")
# listing the iterables
books = list(reader)
for oneBook in books:
    print(oneBook)




# Entry years by the user
startYear = int(input("enter the start year: "))
endYear = int(input("enter the end year: "))

for oneBook in books:

    # Note that we are retrieving onebook from a csv file, therefore it is a string,
    # we therefore have to convert it into a integer fast

    if int(oneBook[2]) in range(startYear, endYear):
        print(oneBook[0])





# check if entry years is within the range and print those books
