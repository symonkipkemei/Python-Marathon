"""
083
Ask the user to type in a word in upper case. If they
type it in lower case, ask them to try again. Keep
repeating this until they type in a message all in
uppercase.
"""



correct = True
while correct:
    msg = input("Type word in uppercase: ")
    msgUpper = str.upper(msg)
    if msg == msgUpper:
        print("Correct")
        correct =False
    else:
        print("Try again")
        correct = True
