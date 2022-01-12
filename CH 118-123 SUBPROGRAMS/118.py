""""
Define a subprogram that will ask the user to
enter a number and save it as the variable
“num”. Define another subprogram that will
use “num” and count from 1 to that number
"""


# GO-GETTER

def number():
    """get number from user"""
    num = int(input("enter a number: "))
    return num
# executer

def count(num):
    """count from one to number"""
    for x in range(1,(num+1)):
        print(x)


def main():
    num = number()
    count(num)

main()