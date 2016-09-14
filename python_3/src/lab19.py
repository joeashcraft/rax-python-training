"""Lab 19 - Character Analysis on Alice in Wonderland.

Use the file alice_in_wonderland.dat to create a Counter.

First, read the entire document into memory, and
remove all whitespace using translate/maketrans.

Then, use a Counter to determine the 20 most used characters in this document.

Print out each character and its number of occurrences in descending order by use count.
"""

from string import maketrans, whitespace, ascii_uppercase, ascii_lowercase
from collections import Counter

PATH_TO_TRAINING_DATA = '/home/student/python-training/python_3/'
with open(PATH_TO_TRAINING_DATA + 'Python III Data/alice_in_wonderland.dat') as bookin:
    book = bookin.read().lower()
    book = book.translate(maketrans('', ''), whitespace)

frequencies = Counter(book)
print frequencies.most_common(20)
