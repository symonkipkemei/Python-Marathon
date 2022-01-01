"""
048
Ask for the name of somebody the user wants to invite
to a party. After this, display the message “[name] has
now been invited” and add 1 to the count. Then ask if
they want to invite somebody else. Keep repeating this
until they no longer want to invite anyone else to the
party and then display how many people they have
coming to the party.
"""
count = 0
invite = "y"
while invite == "y":
    num = str.title(input("Whom do you want to invite to the party?: "))
    print(f"{num} has been invited to the party.")
    count += 1
    invite = str.lower(input("Do you want to invite another person to the party?(Y): "))

print(f"You have invited {count} people to the party.")
