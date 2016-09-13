"""Lab 07 - Lambda Functions.

Take the program tempconversion.py in your data folder containing
a function and replace the function that does the conversion with a
lambda function to do the same thing.
"""


"""tempconversion.py

This program reads a temperature in fahrenheit from
the keyboard, converts it to centigrade (in a function) and prints the
results. Then it requests another input from the keyboard.
"""


# def fahrenheit_to_centigrade(xtmp): return 5.0 / 9.0 * (xtmp - 32)
fahrenheit_to_centigrade = lambda xtmp: 5.0 / 9.0 * (xtmp - 32)

while True:
    temp = raw_input('Enter a temperature: ')
    if temp == 'q' or temp == 'Q':
        break
    try:
        ftemp = float(temp)
    except ValueError:
        print 'Input contains non-numeric data - try again'
        continue
    ctemp = fahrenheit_to_centigrade(ftemp)
    print '{:.1f} degrees Fahrenheit is {:.1f} degrees Centigrade'.format(
        ftemp, ctemp)
