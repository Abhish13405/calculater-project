# calculater-project
this repo is for calculater


 Explanation (For GitHub README)
 About the Project

This is a simple calculator program in Python that takes two numbers from the user and performs basic arithmetic operations using Python’s match-case statement (introduced in Python 3.10).

It supports:

Addition (+)

Subtraction (-)

Multiplication (*)

Division (/)

If the user enters an invalid operator, it will show an error message.

Begins a block of code where errors might happen (like typing letters instead of numbers).

If error occurs, program jumps to except.


Asks the user for the first number.

input() takes input as string.

int(...) converts it to integer.

Stores the value in variable a.
Same as above, but stores second number in b.

Displays the menu of available operations.

\n creates a new line for better readability.
Takes user input for the operator (like +, -, *, /).

Stores it in variable o.
Starts a match-case block (Python’s version of switch).

It compares the value of o with each case.
If the user typed "+", this block executes.

Calculates a+b and prints the result.

f"..." is an f-string that allows {a+b} to be replaced with the actual value.
Executes if the user typed "-".

Subtracts b from a.
Executes if the user typed "*".

Multiplies a and b.
Executes if the user typed "/".

Divides a by b (result is always a float).
Default case (like else).

Runs when no valid operator is entered.
Handles errors (for example: if the user types "abc" instead of a number).

Prevents the program from crashing.


Enter first number: 20
Enter second number: 5
What kind of operation do you want to perform?
+ for addition
- for subtraction
* for multiplication
/ for division
Enter any operation: *
The result is: 100
