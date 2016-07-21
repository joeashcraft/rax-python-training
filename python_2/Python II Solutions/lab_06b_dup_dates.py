""" lab_03d_dup_dates.py

This program generates 23 random integers in the range 1 to 365
inclusive.  Then it checks to see if any of these numbers, which
represent dates, are duplicates. It does this by using the count
method for each item in the list.  Any count that is greater than
one represents a duplicate.
See exercise 10-8 on page 118 in **Think Python**
"""

from random import randint
def has_duplicates(the_list):

    """ Checks given list for duplicates and returns True if so """

    
    if len(the_list) == len(set(the_list)):
        return True
    else:
        return False

same_birthday_counter = 0
trials = 100
for trial in range(trials):
    birthdays = []
    for b in range(23):
        birthdays.append(randint(1, 365))
    if has_duplicates(birthdays):
        same_birthday_counter += 1
print "{0:d} sets of 23 people had the same birthday in {1:d} trials".format(
    same_birthday_counter, trials)



