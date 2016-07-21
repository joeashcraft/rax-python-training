"""lab_02c_ordchr.py

This program prints the ASCII characters corresponding to the
numbers 32 through 126.  Then, from the string module, it imports
a string of all printable (including whitespace) characters. It prints
these out on separate lines along with their corresponding ordinal.
The printing uses "r" formatting which creates a printable representation
of all characters so you can see the whitespace rather than have
these control characters acted on.
"""

from string import printable

for temp_num in range(32, 127):
    print chr(temp_num),
print
raw_input('Press enter to continue')

for temp_chr in printable:
    print '{0!r:6} {1:d}'.format(temp_chr, ord(temp_chr))
    # print '%6r %d' % (temp_chr, ord(temp_chr)) # Older formatting
    

