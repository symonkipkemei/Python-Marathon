"""
069
Create a tuple containing the names of five countries and display the whole tuple. Ask
the user to enter one of the countries that have been shown to them and then display
the index number (i.e. position in the list) of that item in the tuple


"""



countries = ("Kenya", "Uganda", "Ethopia", "Rwanda", "China")
print(countries)

selection = input("Select one of the countries above: ")

for x in countries:
    if selection == x:
        print(countries.index(x))


