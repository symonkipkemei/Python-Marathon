"""
106
Create a new file called “Names.txt”. Add five names to the
document, which are stored on separate lines. Once you have
run the program, look in the location where your program is
stored and check that the file has been created properly.
"""

file = open("names.txt", "w")

for v in range(0,5):
    name = input("enter your name: ")
    file.write(name + "\n")

file.close()