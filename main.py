# Examples: Find whether an entered number is prime or not.

print('This app checks if the number is prime or not')
from math import sqrt


def inputRangeFuction(initialNumb, finalNumb):                  # Modified function signature
    """
    This function generates a list of numbers within a given range.
    """
    try:
        rangeDic = []                                           # Create a new list inside the function
        if initialNumb <= finalNumb:
            for i in range(initialNumb, finalNumb):
                rangeDic.append(i)
            print(rangeDic)
            return rangeDic                                     # Return the generated list
    except ValueError:
        print("Enter number. No string.")

try:
    
    initialNumb = int(input('enter first numb: '))
    finalNumb = int(input('enter final numb: '))

    number_list = inputRangeFuction(initialNumb, finalNumb)     # Call the function with arguments and store the result
    
                                                                # Iterate through each number in the list and check if it's prime
    for number in number_list: 
        numberSqrt = int(sqrt(number))                          # Calculate sqrt for the current number
        primeNumber = True

        for i in range(2, numberSqrt + 1):
            if number % i == 0:
                primeNumber = False
                break

        primeDic = []

        if primeNumber:
            for i in range(initialNumb,finalNumb):
                primeDic.append(i)                              # Modified: Use append correctly
            print(f"The number {primeDic} is prime.")
                                                        # Added a print statement to the else block.
        
except ValueError:
    print('try again with numbers.')


if __name__ == "__main__":
    pass # Remove main() as it's not defined