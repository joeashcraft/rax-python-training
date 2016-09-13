"""Lab 11 - Recursion.

Write a program to calculate a factorial recursively. In mathematics, the
factorial of a positive integer n is denoted by n! and is the product of all
positive integers less than or equal to n.

For example:
    4! = 4 * 3 * 2 * 1 and
    5! = 5 * 4 * 3 * 2 * 1 and so on.

Your program should receive an integer from the keyboard and use a recursive
function to resolve it.
"""


def my_factorial(n):
    result = 1
    if n > 1:
        result *= n
        # n -= 1
        return n * my_factorial(n - 1)
    else:
        return result

"""n! =
factorial(n):
n * (n-1) ...
"""
int_in = int(raw_input("enter an integer: "))

if isinstance(int_in, int):
    # then calc factorial
    print my_factorial(int_in)
else:
    print "quitting"
