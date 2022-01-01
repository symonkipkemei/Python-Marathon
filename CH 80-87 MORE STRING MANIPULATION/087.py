"""
087
Ask the user to type in a word and then
display it backwards on separate lines. For
instance, if they type in “Hello” it should
display as shown below:
"""

wrd = input("Enter word: ")
count = len(wrd)
neWrd = wrd[count:: -1]
print(neWrd)


for x in neWrd:
    print(x)