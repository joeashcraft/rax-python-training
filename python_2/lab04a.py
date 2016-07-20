""" Lab 04a.

1. Implement a stack using a list data type. Pushing five elements
onto the stack. Then, remove each item by using the built-in list
method pop(). Print the stack at each change.

2. Implement a queue using a list. Insert 5 elements onto the
queue using the insert() method and empty the queue using
the pop() method. Print the queue at each change.
"""

my_stack, my_queue = [], []

print "My Stack"

for i in range(1, 6):
    my_stack.append(i)
    print my_stack

for i in range(len(my_stack)):
    my_stack.pop()
    print my_stack

print "My Queue"

for i in range(1, 6):
    my_queue.insert(0, i)
    print my_queue

for i in range(len(my_queue)):
    my_queue.pop()
    print my_queue
