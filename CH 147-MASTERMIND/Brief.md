# Brief

You are going to make an on-screen version of the board game “Mastermind”. The
computer will automatically generate four colours from a list of possible colours (it should
be possible for the computer to randomly select the same colour more than once). For
instance, the computer may choose “red”, “blue”, “red”, “green”. This sequence should not
be displayed to the user.

After this is done the user should enter their choice of four colours from the same list the
computer used. For instance, they may choose “pink”, “blue”, “yellow” and “red”.
After the user has made their selection, the program should display how many colours they
got right in the correct position and how many colours they got right but in the wrong
position. In the example above, it should display the message “Correct colour in the correct
place: 1” and “Correct colour but in the wrong place: 1”.
The user continues guessing until they correctly enter the four colours in the order they
should be in. At the end of the game it should display a suitable message and tell them how
many guesses they took.

#ARCHITECTURE
1. Go getter (RandomColors)
2. Go getter (userInput)
3. Assassin ( check if they got in right position, numbers in correct and wrong position)
4. Assassin (No of tries made)
5. Main( compiler)

