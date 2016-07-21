"""lab_06a_count.py

This program counts all of the printable, non-whitespace characters
and prints them out in descending order of occurrence.  The source
data is the book, "Alice in Wonderland."
"""

from string import ascii_uppercase, digits, punctuation

char_cnt = {}
all_chars = ascii_uppercase + digits + punctuation
# fin = open('/home/student/pydata/alice_in_wonderland.dat') # Linux
fin = open('c:/pydata/alice_in_wonderland.dat')  # Windows file
bookin = fin.read()
bookin = bookin.upper()
for char in bookin:
    if char in all_chars:
        if char in char_cnt:
            char_cnt[char] += 1
        else:
            char_cnt[char] = 1

unload = zip(char_cnt.values(), char_cnt.keys())
unload.sort()
unload.reverse()
iter_count = 0
line_count = 0
for count, character in unload:
    iter_count += 1
    if iter_count > 30:
        break
    print '{0:s} {1:6,d}   '.format(character, count),
#    print '%s %6d   ' % (character, count), # Older formatting - Didn't
#           include the thousands separators in this case.
    line_count += 1
    if line_count >= 5:
        line_count = 0
        print

fin.close()

    
