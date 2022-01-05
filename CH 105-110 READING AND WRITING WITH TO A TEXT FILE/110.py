"""
110
Using the Names.txt file you
created earlier, display the list of
names in Python. Ask the user to
type in one of the names and then
save all the names except the one
they entered into a new file called
Names2.txt.
"""


#open the file first
file = open("names.txt", "r")
print(file.read())
# user to type one of the names
userChoice = input("input name : ")

# New python file

for x in file:
    file2 = open("names2.txt", "a")
    if userChoice != x:
        record = x
        file2.write(x)
    file2.close()




file2 = open("names2.txt", "r")
print(file2.read())

