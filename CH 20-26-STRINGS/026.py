"""
026
Pig Latin takes the first consonant of a word,
moves it to the end of the word and adds on an
“ay”. If a word begins with a vowel you just add
“way” to the end. For example, pig becomes igpay,
banana becomes ananabay, and aadvark becomes
aadvarkway. Create a program that will ask the
user to enter a word and change it into Pig Latin.
Make sure the new word is displayed in lower case.
"""

print("Welcome to pig latin a very interesting game!\nHope you enjoy!")

userWord = input("enter a word: ")
print(userWord[0])

if userWord[0] == "a" or userWord[0] == "e" or userWord[0] == "e" or userWord[0] == "0" or userWord[0] == "u":
    print(userWord+"way")
else:
    length = len(userWord)
    moveWord = userWord[0]
    editedWord = userWord[1:length]
    print(userWord)
    newWord = editedWord+ moveWord + "ay"
    print(newWord)
