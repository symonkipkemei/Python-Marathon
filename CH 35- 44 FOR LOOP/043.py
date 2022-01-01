"""
043
Ask which direction the user wants to count (up or down). If they select up, then ask
them for the top number and then count from 1 to that number. If they select down, ask
them to enter a number below 20 and then count down from 20 to that number. If they
entered something other than up or down, display the message “I don’t understand”.

"""

count = str.lower(input("which direction do you want to count? (up/down): "))

if count == "up":
    numTop = int(input("What's the top number: "))
    for y in range(1, numTop+1):
        print(y)
elif count == "down":
    numBelow = int(input("Enter number below 20: "))
    for x in range(20, numBelow-1, -1):
        print(x)
else:
    print("I don't understand")
