"""
022
Ask the user to enter their first name and surname in lower
case. Change the case to title case and join them together.
Display the finished result.

"""
firstName = input("Enter your first name in lower case: ")
surName = input("Enter your surname in lower case: ")

firstName = str.title(firstName)
surName = str.title(surName)

print(firstName+surName)
