"""Lab 05a.

This program converts one temperature from fahrenheit to centigrade (in a void
or fruitless function) and prints the results.

Change it to handle a variable number of temperatures to covert and print in
the function.
"""

def fahrenheit_to_centigrade(*args):
    print args, type(args)
    for i in args:
        if isinstance(i, (int, float)):
            nutmp = 5.0 / 9.0 * (i - 32)
            print '%.1f degrees Fahrenheit is %.1f degrees Centigrade' % (i, nutmp)
        else:
            print type(i), i

fahrenheit_to_centigrade(72, -10.5, 'a', 111, 55, True, False)
