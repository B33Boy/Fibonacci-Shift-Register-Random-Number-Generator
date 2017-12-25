# Author: Abhi Patel
# Date: 12/24/17
# Purpose: To implement a Fibonacci LSFR (Linear Feedback Shift Register) which is used to generate a sequence of pseudo-random integers from 0 to p-1.


# size - determines the size of the sequence the user wants
# x0 is the first element in the sequence; it must be an integer between 0 and (p-1)
# x1 is the second element in the sequence; it must be an integer between 0 and (p-1)
# p is the maximum possible value that can be generated


# Note that x0 and x1 must fall within the range [0, (p-1)].
# Note that since this is a "discrete-time chaotic dynamical system", the sequence repeats if the array size is large enough


def generateLSFR(size, x0, x1, p):

    # Create an array of given size & set variables
    A = [0] * size

    A[0] = int(x0)
    A[1] = int(x1)

    # Generate the rest of the elements via the following algorithm:
    # Set x[n+1] = (x[n] + x[n-1]) % p where n is 1,2,3,...
    for i in range(1, size-1):
        A[i+1] = (A[i] + A[i-1]) % p

    return A


def run():
    size = int(input("Enter the desired sequence size: "))

    # Test the function
    # One period with the following arguments looks like: 3, 7, 10, 2, 12, 14, 11, 10, 6, 1, 7, 8, 0, 8, 8, 1, 9, 10, 4, 14, 3, 2, 5, 7, 12, 4, 1, 5, 6, 11, 2, 13, 0, 13, 13, 11, 9, 5, 14, 4
    sequence = generateLSFR(size, 3, 7, 15)
    print(sequence)


if __name__ == '__main__':
    run()
