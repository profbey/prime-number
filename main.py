print('This app checks if the number is prime or not')

from math import sqrt

def inputRangeFunction(initialNumb, finalNumb):     # Creates a list containing numbers in the specified range.
    
    rangeList = []
    for i in range(initialNumb, finalNumb + 1):     # Added +1 for inclusion of finalNumb
        rangeList.append(i)
    return rangeList



def find_primes_in_range(initialNumb, finalNumb):   # Finds prime numbers in the specified range and returns them as a list.
    
    primeList = []
    for number in inputRangeFunction(initialNumb, finalNumb):
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
            primeList.append(number)                # Add the prime number to the primeList list

    return primeList




try:                                                # Get input from user
    initialNumb = int(input('Enter starting number: '))
    finalNumb = int(input('Enter the ending number: '))

                                                    # Find and print prime numbers
    prime_numbers = find_primes_in_range(initialNumb, finalNumb)
    print(f"Prime numbers in the specified range: {prime_numbers}")

except ValueError:
    print('Please enter a number.')


# At this stage, the last print(prime_numbers) value must be exported as a .txt file.
# When exporting the .txt file, the name should be 'primeNumbTXT_{initial Numb}_{finalNumb}.txt'

## Two options should be given as query and generation with the interface. 
## According to the selection, two different code directories should be run.