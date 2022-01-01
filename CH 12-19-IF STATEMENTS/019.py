"""
019
Ask the user to enter 1, 2 or 3. If they enter a 1, display
the message “Thank you”, if they enter a 2, display
“Well done”, if they enter a 3, display “Correct”. If
they enter anything else, display “Error message”.
"""

num = int(input("enter 1, 2 or 3: "))

if num == 1:
    print("Thank you")
elif num == 2:
    print("well done")
elif num == 3:
    print("correct")
else:
    print('error message')