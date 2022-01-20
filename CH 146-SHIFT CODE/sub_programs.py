def user_Word():
    """ Get the parameters from the user"""
    userWord = str.lower(input("create a code(word/text):"))
    return userWord


def shift():
    """Insert the number to shift by"""
    gear = int(input("Insert the number to move by: "))
    return gear


def alphabet_data():
    """ the standard alphabet"""
    # The alphabet should extend beyond z so that alphabets loop beyond it
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz ,'. ,'. ,'. ,'. ,'. ,'."
    return alphabet


def coder(userWord, gear, alphabet):
    """code the word insert by the user """
    codedWord = ""
    for y in userWord:
        # establish the position of the word in alphabet
        originalPosition = alphabet.index(y)
        # establish the new position
        newPosition = originalPosition + gear
        # determine the new alphabet derived from the new position
        newWord = alphabet[newPosition]
        # (concatenate) new word to an empty string
        codedWord += newWord

    print(f"The coded message is \n{codedWord}")
    return codedWord


def decoder(codedWord, gear, alphabet):
    """ this code takes the coded message and decodes to a normal word"""
    # declare the original sentence as an empty string
    originalSentence = ""

    for x in codedWord:
        # determine the position of the coded alphabet in the alphabet string
        codedPosition = alphabet.index(x)
        # determine the original position
        originalPosition = codedPosition - gear
        # determine the original word
        originalWord = alphabet[originalPosition]
        # originalSentence
        originalSentence += originalWord

    print(f"The decoded message is \n{originalSentence}")

