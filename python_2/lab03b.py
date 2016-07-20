"""Lab 03b - Filter, Map, Reduce.

* Use the range function to create a list containing the numbers:
    [2, 5, 8, 11, 14, 17]

*   Use the techniques you have learned so far to:
    *   Create and print a new list with only the even numbers from the
original list. (filter)
    *   Create and print another new list containing the square of the
original numbers. (map)
*   Create a result showing the sum of all the original numbers.
(reduce)
* Use normal loops to accomplish each of these tasks
"""

# initialize vars
my_list, even_list, sqr_list = [], [], []
total = 0

# create first list
my_list = range(2, 18, 3)
print "first list",
print my_list

# create and print new list with only evens from original list
for x in my_list:
    if x % 2 == 0:
        even_list.append(x)
print "evens list",
print even_list

# Create and print another new list containing the square of
# the original numbers. (map)
for y in my_list:
    sqr_list.append(y**2)

print "squares list",
print sqr_list

# Create a result showing the sum of
# all the original numbers. (reduce)
for z in my_list:
    total += z
print "sum of items in original list: {0:d}".format(total)
