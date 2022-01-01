"""
082
Show the user a line of text from your favourite poem
and ask for a starting and ending point. Display the
characters between those two points.
"""
love = "Kisses for girls, love for boys"
print(love)

start = int(input("Enter start point: "))
end = int(input("Enter end point: "))


print(love[start:end])


