"""
075
Create a list of four three-digit
numbers. Display the list to the
user, showing each item from
the list on a separate line. Ask
the user to enter a three-digit
number. If the number they
have typed in matches one in
the list, display the position of
that number in the list,
otherwise display the message
“That is not in the list”
"""


num = [456, 879, 657, 435]
for x in num:
    print(x)


userNum = int(input("Enter a 3 digit number:"))


count = 0
for x in num:
    if x == userNum:
        print(f"The number is position {num.index(x)}")
        count = 0
    else:
        count += 1

if count == len(num):
    print("That is not in the list")



