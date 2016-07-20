"""Lab 03d.

If there are 23 students in your class, what are the chances that two
of you have the same birthday? You can estimate this probability by
generating random samples of 23 birthdays and checking for
matches.

Write the program such that you run the exercise at least 100 times.
At the conclusion of the program print the number of times duplicate
dates were detected. As suggested in the book, use the randint
function in the random module to generate numbers from 1 to 365 to
simulate dates.
"""

from random import randint
duplicates_counter = 0
group_size = 23
trials = 100


def has_duplicates(my_list):
    """True if a list has duplicates.

    return True if my_list contains a duplicate int(value).
    otherwise return False.
    """
    for i in my_list:
        if my_list.count(i) > 1:
            return True
    return False

for x in range(trials):
    birthdays = []
    for i in range(group_size):
        birthdays.append(randint(1, 365))

    if has_duplicates(birthdays):
        duplicates_counter += 1
print "{:d} duplicates found".format(duplicates_counter)
