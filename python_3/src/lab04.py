"""Lab 04.

Modify the results of the Lab02 (available online) to print just the top
20 words along with their respective use counts.
Print them in descending order by use count.
Do the sorting in one statement using the capabilities we have just reviewed. It isn't necessary to print all
the data we have printed previously.

The objective here is to ensure you can sort using the capabilities we just reviewed.
Also remember, you must unload the dictionary in order to sort the contents.
"""

from string import punctuation, maketrans
from operator import itemgetter

# file = open('/Users/joe6623/Training/python/python_2/Python II Data/alice_in_wonderland.dat', 'r')
file = open('/home/student/python-training/python_2/Python II Data/alice_in_wonderland.dat', 'r')
bookin = file.read().lower()
file.close()

# file = open('/Users/joe6623/Training/python/python_2/Python II Data/words.txt', 'r')
file = open('/home/student/python-training/python_2/Python II Data/words.txt', 'r')
wordsin = file.read().lower()
file.close()

## Create a dictionary for counting using the entries from words.txt as the keys.
# dictionary = {'word': int(count)}
dictionary = dict.fromkeys(wordsin.split(), 0)

## Parse the text in alice_in_wonderland.data isolating each word.
##   This requires removing/replacing all punctuation and using the split method.
bookin = bookin.translate(maketrans(punctuation, ' ' * len(punctuation)), "'")

book = list()
for word in bookin.split():
    book.append(word)

book_set = set(book)
unfound_words = set()
good_words = {}

## Find each word from the book in your dictionary and increase the count for that word by one.
for word in book_set:
    if word in dictionary:
        good_words[word] = book.count(word)
    ## If a word is not found in the dictionary, place it in a list with other unfound words.
    else:
        # word goes in to SET of unfound words
        unfound_words.add(word)

# DEBUG
# print type(book)
# print type(book_set)
# print book[0:4]
#
# for i in range(4):
#     print "{} is a good word".format(list(good_words.keys())[i])
# # print "adventures used {} times.".format(good_words['adventures'])
# for i in range(4):
#     print "{} is an unfound word".format(list(unfound_words)[i])
# /DEBUG

sorted_good_words = sorted(good_words.items(), key=itemgetter(1), reverse=True)
print "{} was used the most: {} times.".format(sorted_good_words[-1][1], sorted_good_words[-1][0])

print sorted_good_words[:19]
