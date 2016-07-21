"""lab_05b_argv.py

This program reads a variable number of fahrenheit temperatures from
the command line and converts them to centigrade.  Note - it skips the
first parameter.

"""

from sys import argv

def f_to_c(*args):
    print(type(args), args) 
    for parm in args:
        try:
            temp = float(parm)
            cent_temp = 5.0 / 9.0 * (temp -32)
            print('{0:6.1f} {1:5.1f}'.format(temp, cent_temp))
#            print '%6.1f %5.1f' % (temp, cent_temp) Older formatting
        except ValueError:
            print(parm, 'This data is not valid')

print(type(argv), argv)
f_to_c(*argv[1:])  # send all but the first parameter to the function
#  And send them as individual arguments, not in a tuple


