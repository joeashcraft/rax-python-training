"""Lab 06a.

Read the book "Alice in Wonderland" into memory.

Create a dictionary counting all the printable characters excluding whitespace.

Be sure not to count upper- and lower-case letters separately.

When done, print the top 30 most frequently occurring characters along with the
number of occurrences.

Creating the dictionary is the most important part of this lab.

If you have time, print five character/occurrences combinations
per line. Make sure all the elements of the printed lines form
neat columns.
"""
from string import printable, whitespace

file = open('./Python II Data/alice_in_wonderland.dat', 'r')
bookin = file.read().lower()
file.close()
# print type(bookin)

dict = {}
for x in bookin:
    if x in printable and x not in whitespace:
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1
    else:
        continue
# print type(dict)
# print dict

dict_to_sort = []
for x, y in dict.items():
    dict_to_sort.append([int(y), x])

dict_sorted = list(reversed(sorted(dict_to_sort)))

for i in range(30):
    print dict_sorted[i]
