"""lab_03a_probability_alt.py

This program simulates rolling a pair of dice 100,000 times and
calculates the percentage of the time each possible roll occurs.
These results are then compared to the mathematically derived
results.
"""

from random import randrange
def dice_roll():
    return randrange(1, 7) + randrange(1, 7)

roll_lst = 13 * [0]  # positions 0 and 1 will never be used.
rolls = 100000
for i in range(rolls):
    roll_lst[dice_roll()] += 1  # The result of the function is used
                                # directly as an index
roll = 2
for i in roll_lst[2:]:
    print '{0:2d} {1:6.2%}'.format(roll, float(i) / rolls)
#    print '%2d %5.2f%%' % (roll, i * 100.0 / rolls) # Older formatting
#    Note the use of %% to insert the percent sign in the result
    roll += 1

    
    
