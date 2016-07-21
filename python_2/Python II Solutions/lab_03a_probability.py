"""lab_03a_probability.py

This program simulates rolling a pair of dice 100,000 times and
calculates the percentage of the time each possible roll occurs.
These results are then compared to the mathematically derived
results.  This program is an example of wasting time to save a
trivial amount of memory
"""

from random import randrange
def dice_roll():
    return randrange(1, 7) + randrange(1, 7)

roll_lst = 11 * [0]
rolls = 100000
for i in range(rolls):
    j = dice_roll()
    roll_lst[j-2] += 1
roll = 2
for i in roll_lst:
    tmp = float(i) / rolls
#    tmp = i * 100.0 / rolls
    print '{0:2d} {1:6.2%}'.format(roll, tmp)
#    print '%2d %5.2f%%' % (roll, tmp)
    roll += 1
    
