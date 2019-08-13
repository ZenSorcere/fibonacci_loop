# Name: fibonacci_loop.py
# Description: program that will calculate the nth position of the Fibonacci
#    sequence. User enters the nth position, and a loop will determine what
#    number in the sequence that is.
# Author:  Mike Gilson
# Date: 8/8/19


# Define main, state to user the purpose of the program, and added line break.
def main():
    print("This program caclulates the nth value of the Fibonacci Sequence. \n")

# Get user input for which placement in the Fib sequence they are requesting. 
    n = int(input("Enter the position in the Fibonacci sequence (integer above 0):  "))

# If/Else statement: for values of 1 and 2, display the specific answer.
# For 0, dislay they didnt follow directions.
    if n == 0:
        print ("\nI said ABOVE 0...")
    elif n == 1:
        print ("\nThat would be 1.")
    elif n == 2:
        print ("\nThat would be 1.")

# For the else statement, I instituted a FOR loop, using the formula for the
#   Fibonacci sequence as individual variables (a=(n-1) and b = (n-2), essentially),
#   two  initially defined with the firstelements of the sequence, 0 and 1.
# Range of "n-1" is for n values of 3 or higher.
# the FOR loop thus continually updates the values for a and b, so the loop
#   continually adds two previous numbers in the sequence to arrive at the next one.
    else:
        a = 0
        b = 1
        for i in range(n-1):
            c = a+b
            a = b
            b = c

# Display the final value of c to the user (which is the answer).           
        print ("\nThat would be " + str(c) + ".")   

# Guarantees that the main will automatically run when the program is
#     invoked directly, but not if the module is imported.
if __name__ == '__main__':
    main()





