"""lab_05a_parms.py

This program takes a variable number of fahrenheit temperatures from
the main program and converts them to centigrade in a function. Note
how the values of True and False are interpreted
"""

def f_to_c(*args):
    
    print type(args), args
    for temp in args:
        if isinstance(temp, (int, float)):            
            cent_temp = 5.0 / 9.0 * (temp -32)
            print '{0:6.1f} {1:5.1f}'.format(temp, cent_temp)
#            print '%6.1f %5.1f' % (temp, cent_temp) # Older formatting
        else:
            print temp, 'This data is not valid'


a = 12.3
b = 110
c = 'text'
d = -2
f_to_c(a, 56, b, c, d, b - a, True, False)

