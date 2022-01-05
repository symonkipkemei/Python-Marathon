"""
109
Display the following menu to the user:
Ask the user to enter 1, 2 or 3. If they select
anything other than 1, 2 or 3 it should display a
suitable error message.
If they select 1, ask the user to enter a school
subject and save it to a new file called
“Subject.txt”. It should overwrite any existing f
with a new file.
If they select 2, display the contents of the
“Subject.txt” file.
If they select 3, ask the user to enter a new
subject and save it to the file and then display
the entire contents of the file.
Run the program several times to test the
"""

print("(1) Create a new file\n"
      "(2) display the file\n"
      "(3) add a new item to the file\n")
selection = int(input("make a selection 1, 2, 3:"))

if selection == 1 or selection == 2 or selection == 3:
    if selection == 1:
        subject = input("enter a school subject: ")
        file = open("Subject.txt", "w")
        file.write(subject)
        file.close()
    elif selection == 2:
        file = open("Subject.txt", "r")
        print(file.read())
        file.close()
    else:
        newSubject = input("insert new subject : ")
        file = open("Subject.txt", "a")
        file.write(newSubject + "\n")
        file.close()

        file = open("Subject.txt", "r")
        print(file.read())
        file.close()
else:
      print("you entered a wrong value, try again.")
