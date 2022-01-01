"""
079
Create an empty list called “nums”.
Ask the user to enter numbers.
After each number is entered, add
it to the end of the nums list and
display the list. Once they have
entered three numbers, ask them if
they still want the last number they
entered saved. If they say “no”,
remove the last item from the list.
Display the list of numbers.
"""

nums = []


for x in range(0,3):
    userNum = int(input("Enter number: "))
    nums.append(userNum)

print(nums)

save = input("Do you still want the last number saved (y)es or (n)o: ")


if save == "n":
    nums.remove(len(nums))
    print(nums)

else:
    print(nums)