#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

:mod:`lab_pyreview` -- Python review
=========================================

LAB PyReview Learning Objective: Review the topics from the previous courses

a. Load the data from the two dictionary files in the data directory into two
   list objects.  data/dictionary1.txt data/dictionary2.txt
   Print the number of entries in each list of words.

b. Use sets in Python to merge the two lists of words with no duplications (union).
   Print the number of words in the combined list.

c. Import the random library and use one of the functions to print out five random
   words from the combined list of words.

d. Use a list comprehension to find all the words that start with the letter 'a'.
   Print the number of words that begin with the letter 'a'.

e. Create a function called wordcount() with a yield that takes the list of
   all words as an argument and yields a tuple of
   (letter, number_of_words_starting_with_that_letter) with each iteration.

"""

# PART A
with open("../RU_Python_IV/data/dictionary1.txt", "r") as dictionary1, \
     open("../RU_Python_IV/data/dictionary2.txt", "r") as dictionary2:
    dict1 = dictionary1.readlines()
    dict2 = dictionary2.readlines()

print("dictionary 1 contains ", len(dict1), "words.")
print("dictionary 2 contains ", len(dict2), "words.")

# PART B
combined = set(dict1 + dict2)
print("combined list contains", len(combined), "unique words.")
combined_lst = list(combined)

# PART C
print("5 Random Words")
from random import randint
for ii in range(5):
    print(combined_lst[randint(0, len(combined_lst))], end='')

# PART D
a_lst = [x for x in combined_lst if x[0] == "a"]
print(len(a_lst), "words begin with 'a'")

# PART E
from string import ascii_lowercase


def wordcount(all_words):
    for ii in ascii_lowercase:
        count = 0
        for w in all_words:
            if w[0] == ii:
                count += 1
        yield ii, count


x = wordcount(combined_lst)
print(next(x))
