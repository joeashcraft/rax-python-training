"""lab_06a_list.py

This program counts all of the printable, non-whitespace characters
and prints them out in descending order of occurrence.  The source
data is the book, "Alice in Wonderland."  This version of the
program uses a two-dimensional list instead of a dictionary.  It
demonstrates the use of the else option in a looping statement.
The else option is always executed except when a break is issued
to end the loop.  In this case, the else option is executed when
we don't find the character in the list.  Note also, the count is
placed first in the low-order list.  This makes sorting on the
character count easier.
"""

from string import ascii_uppercase, digits, punctuation

char_cnt = []
all_chars = ascii_uppercase + digits + punctuation
fin = open('/home/student/pydata/alice_in_wonderland.dat') # Linux
# fin = open('c:/pydata/alice_in_wonderland.dat')  # Windows file
bookin = fin.read()
bookin = bookin.upper()
for char in bookin:
    if char not in all_chars:
        continue
    for x in char_cnt:
        if x[1] == char:
            x[0] += 1
            break
    else:  # The seldom-used else option is useful here.
        char_cnt.append([1, char]) #Add a sublist for the new character

unload = reversed(sorted(char_cnt))
iter_count = 0
line_count = 0
for count, character in unload:
    iter_count += 1
    if iter_count > 30:
        break
    # This version of the program uses only the older formatting
    print('%s %6s   ' % (character, format(count, ',d')), end=' ')
    line_count += 1
    if line_count >= 5:
        line_count = 0
        print()

fin.close()

    
