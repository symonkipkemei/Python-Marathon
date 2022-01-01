"""
076
Ask the user to enter the names of three people they want to
invite to a party and store them in a list. After they have entered
all three names, ask them if they want to add another. If they do,
allow them to add more names until they answer “no”. When
they answer “no”, display how many people they have invited to
the party
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


