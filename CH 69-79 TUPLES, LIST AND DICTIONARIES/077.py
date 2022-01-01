"""
077
Change program 076 so that once the user has completed their list of names, display the
full list and ask them to type in one of the names on the list. Display the position of that
name in the list. Ask the user if they still want that person to come to the party. If they
answer “no”, delete that entry from the list and display the list again.
"""

party = []
for x in range(0,3):
    invitee = str.title(input("Enter name of people you will like to invite to the party: "))
    party.append(invitee)

another = str.lower(input("Would you like to add another (y)es or (n)o:"))

while another == "y":
    invitee = str.title(input("Enter the invited guest: "))
    party.append(invitee)
    another = str.lower(input("Would you like to add another (y)es or (n)o:"))

print(f"You have invited {len(party)} to the party they are: ")
for x in party:
    print(x)

userType = str.title(input("Type the name of the person in the list: "))

print(party.index(userType))


userChoice = str.lower(input("Do you still want the guest above in the party (y)es or (n)o: "))

if userChoice == "n":
    party.remove(userType)
