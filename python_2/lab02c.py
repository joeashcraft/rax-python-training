"""lab02c.py

Using the chr() and ord() built-in functions, print the ASCII characters
corresponding to the numbers 32 through 126.

Then, from the string module, import the variable printable. If necessary,
review the string module through help('string') in the shell or pydoc string
from command line.

Afterwards, iterate through the "printable" string and print out each entry and
its corresponding ordinal. Be sure to use !r ( or the older %r) formatting on
the string items so you can see the whitespace characters.
"""

from string import printable

for i in range(32, 127):
    print chr(i),

for x in printable:
    print "%-9r %03d" % (x, ord(x))
