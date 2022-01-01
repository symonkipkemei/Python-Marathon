"""
071
Create a list of two sports. Ask the
user what their favourite sport is and
add this to the end of the list. Sort the
list and display it.
"""

sports = ["Football", "Rugby"]

userSport = input("What is your favorite sport?: ")

sports.append(userSport)
sports.sort()
print(sports)