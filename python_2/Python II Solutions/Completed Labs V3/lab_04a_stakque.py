""" lab_04a_stakque.py

Build a push-down stack with five elements (numbers 1 - 5) and print
the stack at each change.  Then remove the elements in LIFO fashion
using the pop() method.  Then implement a queue inserting elements
such that when the pop() method is employed, the elements are
removed in FIFO fashion.  Again, the queue is printed at each change.
"""

my_stack = []
for i in range(1, 6):
    my_stack.append(i) # Build the stack with append
    print(my_stack)
for i in range(len(my_stack)):
    my_stack.pop() # pop() takes the last item giving us LIFO
    print(my_stack)

my_queue = []
for i in range(1, 6):
    my_queue.insert(0, i) # Insert each item at the front of the list
    print(my_queue)
for i in range(len(my_queue)):
    my_queue.pop() # pop() takes the last item giving us FIFO
    print(my_queue)

