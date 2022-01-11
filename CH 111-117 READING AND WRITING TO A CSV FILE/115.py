"""
Using the Books.csv file, display the data in
the file along with the row number of each.
"""

#import csv

import csv

# open csv file

file = open("Books.csv", "r")

# convert into an iterable

reader = csv.reader(file)

# list the iterables
rows = list(reader)

for index, row in enumerate(rows):
    print(f"{index}. {row}")

    