"""Lab 02.

Go back to the last lab and use the translate method to deal with the
replacement or removal of punctuation.
Also, create the dictionary from words.txt by using the fromkeys method.

Instructor's version of the last lab is available online.
"""

from string import punctuation, maketrans

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


## When you have processed the entire book, determine the percentage of words in the dictionary that were used in the book

# how many words in word list?
print "Words in dictionary:  {}".format(len(dictionary))
# how many good words used in book?
# len(good_words.values())

print "Good words in book:  {}".format(len(good_words.values()))
# add all values of good_words{}
print "Percent of book words found in dictionary: {0:.3%}".format(
    float(len(good_words.values()) - len(unfound_words)) / len(dictionary)
)

## and which word was used the most.
sorted_good_words = sorted(zip(good_words.itervalues(), good_words.iterkeys()))
print "{} was used the most: {} times.".format(sorted_good_words[-1][1], sorted_good_words[-1][0])

## Remove the duplicates from the list of unfound words, sort it and print it. Don't try too hard to make this perfect. It won't happen!
print "Unfound Words:  {}".format(len(unfound_words))
# print sorted(list(unfound_words))  # UGLY

# unfound_words = sorted(list(unfound_words))
# for i in range(len(unfound_words)):
#     count = 0
#     while count < 5:
#         print "{}".format(unfound_words[i]),
#         count += 1
#         break
#     print
