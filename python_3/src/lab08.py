"""Lab 08.

Write a generator that returns an increasing integer
if the integer is even or the string "odd" if the integer is odd.

Choose arbitrary starting and stopping points (e.g., 4 and 15). When
the numbers are exhausted, let the function end without a yield
statement.


Test your generator by using a *for* statement and then again by
calling next() and testing for StopIteration manually. Print whatever
is returned from the generator in both cases.
"""


def my_gen(start, stop):
    for x in xrange(start, stop):
        yield x if x % 2 == 0 else "odd"

print "for loop ====="
for x in my_gen(3, 19):
    print x

print "while loop ====="
next_gen = my_gen(13, 23)
while True:
    try:
        print next_gen.next()
    except StopIteration:
        print "Done!"
        break
