"""Lab 03c.

Read the trees.dat file, putting each valid element into a list.

The file contains the height in even feet of a large sample of
California coastal redwood trees. When finished, use only built-
in functions and normal math equations to produce a report on
the screen showing:
* the number of trees,
* the average height of the trees to one decimal place,
* the height of the tallest tree, and
* the height of the shortest tree.
"""

file = open('./Python II Data/trees.dat', 'r')
my_list = []

for linein in file:
    try:
        my_list.append(int(linein))
    except:
        continue

print "number of trees: {:d}".format(len(my_list))
print "average height:  {:.1f}".format(float(sum(my_list))/len(my_list))
print "tallest tree:    {:d}".format(max(my_list))
print "shortest tree:   {:d}".format(min(my_list))
