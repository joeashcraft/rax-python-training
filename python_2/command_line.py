"""command-line parameters.

*   Create the following two-line program:

        from sys import argv
        print type(argv), argv

*   Execute your program from command line twice:

    python progname.py
    python progname.py 2016 04 13
"""
from sys import argv

print type(argv), argv
