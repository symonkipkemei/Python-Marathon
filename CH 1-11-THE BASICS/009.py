"""
009
Write a program
that will ask for a
number of days
and then will
show how many
hours, minutes
and seconds are
in that number of
days.
"""

numofDays = int(input("How many days are there?"))

# The idea is that 1 day is the si unit of measure

#hours

# i day has 24 hours

hoursIn1Day = 24
minutesIn1Day = hoursIn1Day * 60
secondsIn1Day = minutesIn1Day * 60


# hours in number of days
hours = numofDays * hoursIn1Day

# minutes in number of days
minutes = numofDays * minutesIn1Day

# seconds in number of days
seconds = numofDays * secondsIn1Day


print(f"There are {hours} hours, {minutes} minutes and {seconds} seconds in {numofDays} days")

