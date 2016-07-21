"""lab_03b_filtermapred.py

This program provides examples of filter, map and reduce.  These
operations are accomplished a number of ways in Python.  The most
straight-forward way is through simple loops as shown here. Other ways
are shown in Python III.
"""

# This code creates this list [2, 5, 8, 11, 14, 17]
x = range(2,20,3)
print 'Original list:', x

# This loop selects only the even numbers to be included in a new list
# This is an example of filtering.
y = []
for i in x:
    if i % 2 == 0:
        y.append(i)
print y

# This loop creates a new list containing the square of each entry in
# list x.  This is an example of mapping.
y = []
for i in x:
    y.append(i**2)
print y

# This loop sums all of the entries in list x.  It is an example of
# reducing.
y = 0
for i in x:
    y += i
print y

