

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
    for row in file:
        print(row)


def main():
    correct = True
    while correct:
        print("1) add to file\n"
              "2) view all records\n"
              "3) Quit program\n")
        selection = int(input("Enter the number of your selection: "))

        if selection == 1:
            add()
        elif selection == 2:
            read_csv()
        elif selection == 3:
            correct = False
        else:
            print("Incorrect input")

main()
