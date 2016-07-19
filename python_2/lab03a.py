"""lab3a.py

Create a function to simulate the rolling of a pair of dice.

Call this function 100,000 times accumulating the results of each roll in a
list.

When finished, print the percentage of times each possible roll occurred along
with the total number of rolls.

Visually compare your results to the mathematically derived results in the
adjacent table.
"""

from random import randrange
results = 11 * [0]
times_to_roll = 100000


def roll_dice():
    """roll two dice; return sum."""
    return (randrange(1, 7) + randrange(1, 7))

for i in xrange(times_to_roll):
    results[roll_dice()-2] += 1

for x, y in zip(range(2, 13), results):
    print '{0:2d} : {1:6.2%}'.format(x, float(y)/times_to_roll)
    # print "%2d : %5.2f" % (x, 100*float(y)/times_to_roll)
