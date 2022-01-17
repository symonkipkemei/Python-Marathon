## GO-GETTER

def number():
    """get number from user"""
    num = int(input("enter a number: "))
    return num


## EXECUTER

def check_if_prime(inputNum):
    """the functions adds the sum of primes between
    o and a given input"""

    # a prime number is divisible only by itself and 1

    # loop through the numbers, if the number is divisible by
    # any other numbers ( between 2 and (inputNum-1) and returns a modulus of 0 , it is not prime number

    count = 0
    for num in range(2, inputNum):
        if inputNum % num == 0:
            count += 1

    if count == 0:
        return True
    else:
        return False


# COMPILER

def main():
    # number obtained from the user
    num = number()
    # total sum of prime numbers declared
    sumPrime = 0
    # loop through 0 and given input
    for x in range(0, num):
        status = check_if_prime(x)
        # if it is true this number is prime add it to the total sum
        if status:
            sumPrime += x

    # 1 not being a prime number subtract it from the total results
    sumPrime -= 1
    print(f"\nThe total sum of prime numbers is {sumPrime}")


main()
