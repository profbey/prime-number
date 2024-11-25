print('This app checks if the number is prime or not')

from math import sqrt


def inputRangeFunction(initialNumb, finalNumb):     # Creates a list containing numbers in the specified range.
    
    rangeList = []
    for i in range(initialNumb, finalNumb + 1):     # Added +1 for inclusion of finalNumb
        rangeList.append(i)
    return rangeList


def find_primes_in_range(initialNumb, finalNumb):   # Finds prime numbers in the specified range and returns them as a list.
    
    primeDic = []
    for number in n(initialNumb, finalNumb):
        numberSqrt = int(sqrt(number))
        isPrime = True

        if number < 2:                              # Numbers less than 2 are not prime
            isPrime = False
        else:
            for i in range(2, numberSqrt + 1):
                if number % i == 0:
                    isPrime = False
                    break

        if isPrime:
            primeDic.append(number)                 # Add the prime number to the primeDic list

    return primeDic


try:                                                # Getting input from user
    initialNumb = int(input('Enter starting number: '))
    finalNumb = int(input('Enter the ending number: '))

                                                    # Finding and printing prime numbers
    prime_numbers = find_primes_in_range(initialNumb, finalNumb)
    print(f"Prime numbers in the specified range: {prime_numbers}")

except ValueError:
    print('Please enter a number.')