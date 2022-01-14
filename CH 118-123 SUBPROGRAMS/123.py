"""
123
In Python, it is not technically possible to directly
delete a record from a .csv file. Instead you need
to save the file to a temporary list in Python,
make the changes to the list and then overwrite
the original file with the temporary list.
Change the previous program to allow you to do
this. Your menu should now look like this:
"""


def add():
    """ add name an salary to a csv file"""
    import csv
    name = input("insert your name:")
    salary = input("insert your salary:")
    data = name + "," + salary + "\n"
    # choose append mode (a) to avoid overwriting data  in the next entry
    file = open("Salaries.csv", "a")
    file.write(data)
    file.close()


def read_csv():
    import csv
    file = open("Salaries.csv", "r")
    reader = csv.reader(file)
    salaries = list(reader)
    for index, row in enumerate(salaries):
        print(f"{index}. {row})")
    file.close()



def delete_csv():
    import csv
    file = open("Salaries.csv", "r")
    tmp = []

    # save data to a temporary list
    for row in file:
        tmp.append(row)
    print(tmp)
    for index, row in enumerate(tmp):
        print(index, row)

    # delete item form the list
    indexInput = int(input("insert the index of the record you want deleted: "))
    del tmp[indexInput]

    file = open("Salaries.csv", "w")
    # convert list to a csv file
    for row in tmp:
        file.write(row)

    file.close()


def main():
    correct = True
    while correct:
        print("\n1) add to file\n"
              "2) view all records\n"
              "3) Delete a record\n"
              "4) Quit program\n")
        selection = int(input("Enter the number of your selection: "))

        if selection == 1:
            add()
        elif selection == 2:
            read_csv()
        elif selection == 4:
            correct = False
        elif selection == 3:
            delete_csv()

        else:
            print("Incorrect input")

main()
