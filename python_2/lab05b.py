"""Lab 05b.

Create a copy of the program from Lab 05a and change the main program to accept
a variable number of parameters from the command line. Send those parameters to
your function which is still accepting a variable number of inputs. Print all
results.

As before, have the function parse/test the arguments using different tools as
necessary.
"""
from sys import argv
# print type(argv), argv[1:]


def fahrenheit_to_centigrade(*args):
    # print args, type(args)
    for i in args:
        try:
            i = float(i)
        except:
            print "fail on value: {:s}".format(i)
            continue
        nutmp = 5.0 / 9.0 * (i - 32)
        print '%.1f degrees Fahrenheit is %.1f degrees Centigrade' % (i, nutmp)

fahrenheit_to_centigrade(*argv[1:])
