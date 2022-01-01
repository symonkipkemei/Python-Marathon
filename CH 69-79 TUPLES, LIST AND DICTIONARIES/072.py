"""
072
Create a list of six school subjects. Ask the user which of these
subjects they don’t like. Delete the subject they have chosen from the
list before you display the list again.
"""

subjects = ["Christian Religous Education", "Activities", "Hygiene", "Environmental", "Creative Art"]
print(subjects)

userSelection = str.title(input("Which of the above subjects don't you like?: "))

subjects.remove(userSelection)
print(subjects)