"""
023
Ask the user to type in the first
line of a nursery rhyme and
display the length of the string.
Ask for a starting number and an
ending number and then display
just that section of the text
(remember Python starts
counting from 0 and not 1)
"""
rhyme = input("type in the first line of nursery rhyme: ")

print(len(rhyme))

startNum = int(input("Enter the starting number: "))
endNum = int(input("Enter the ending number: "))
print(rhyme[startNum : endNum])
