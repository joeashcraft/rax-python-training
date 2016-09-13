#! env python
"""Python 3 Prereq from Python 2.

In the data from Python II find, "alice_in_wonderland.dat."
You will also find a file labeled, "words.txt." The latter file contains over 100,000 English-language words.

Your job is to perform the following:
* Create a dictionary for counting using the entries from words.txt as the keys.

* Parse the text in alice_in_wonderland.data isolating each word. This requires removing/replacing all punctuation and using the split method.
    * Make sure the words in the book are all lower case.

* Find each word from the book in your dictionary and increase the count for that word by one.
    * If a word is not found in the dictionary, place it in a list with other unfound words.

* When you have processed the entire book, determine the percentage of words in the dictionary that were used in the book,
    * and which word was used the most.

* Remove the duplicates from the list of unfound words, sort it and print it. Don't try too hard to make this perfect. It won't happen!
"""

from string import punctuation, whitespace

# ? split on whitespace and punctuation
# ? which word was used the most

file = open('/Users/joe6623/Training/python/python_2/Python II Data/alice_in_wonderland.dat', 'r')
bookin = file.read().lower()
file.close()

file = open('/Users/joe6623/Training/python/python_2/Python II Data/words.txt', 'r')
wordsin = file.read().lower()
file.close()

## Create a dictionary for counting using the entries from words.txt as the keys.
# words = {'word': int(count)}
dictionary = {}
for word in wordsin.split():
    dictionary[word] = 0

## Parse the text in alice_in_wonderland.data isolating each word.
##   This requires removing/replacing all punctuation and using the split method.
##   Make sure the words in the book are all lower case.
book = []
# sep = punctuation + whitespace
# print sep
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

## DEBUG
# print type(book)
# print type(book_set)
# print book[0:4]
#
# for i in range(4):
#     print "{} is a good word".format(list(good_words.keys())[i])
# # print "adventures used {} times.".format(good_words['adventures'])
# for i in range(4):
#     print "{} is an unfound word".format(list(unfound_words)[i])
##/DEBUG


## When you have processed the entire book, determine the percentage of words in the dictionary that were used in the book

# how many words in word list?
print "Words in dictionary:  {}".format(len(dictionary))
# how many good words used in book?
count = 0
for i in good_words.values():
    count += i

print "Good words in book:  {}".format(count)
# add all values of good_words{}
print "Percent of book words found in dictionary: {0:.3%}".format(float(count)/len(dictionary))

## and which word was used the most.
# count_good_words = []
# for k, v in good_words.items():
#     count_good_words.append([v, k])
#
# print "{} was used the most, {} times.".format(max(count_good_words))

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
