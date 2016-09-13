"""Lab 03.

Go back and change the last lab to send all print statements to a file instead.
Use a with statement to open this file.

Also, if you opened input files such that needed to be explicitly closes,
change these to be open using a with statement as well.
"""

from string import punctuation, maketrans

# file = open('/Users/joe6623/Training/python/python_2/Python II Data/alice_in_wonderland.dat', 'r')
# file = open('/Users/joe6623/Training/python/python_2/Python II Data/words.txt', 'r')
with open('/home/student/python-training/python_2/Python II Data/alice_in_wonderland.dat', 'r') as bookin, \
    open('/home/student/python-training/python_2/Python II Data/words.txt', 'r') as wordsin:
    bookin = bookin.read().lower()
    wordsin = wordsin.read().lower()

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

with open('/home/student/python-training/python_3/lab03.out', 'w') as log_file:
    ## When you have processed the entire book, determine the percentage of words in the dictionary that were used in the book

    # how many words in word list?
    log_file.writelines("Words in dictionary:  {}\n".format(len(dictionary)))
    # how many good words used in book?
    # len(good_words.values())

    log_file.writelines("Good words in book:  {}\n".format(len(good_words.values())))
    # add all values of good_words{}
    log_file.writelines("Percent of book words found in dictionary: {0:.3%}\n".format(
        float(len(good_words.values()) - len(unfound_words)) / len(dictionary)
    ))

    ## and which word was used the most.
    sorted_good_words = sorted(zip(good_words.itervalues(), good_words.iterkeys()))
    log_file.writelines("{} was used the most: {} times.\n".format(sorted_good_words[-1][1], sorted_good_words[-1][0]))

    ## Remove the duplicates from the list of unfound words, sort it and print it. Don't try too hard to make this perfect. It won't happen!
    log_file.writelines("Unfound Words:  {}\n".format(len(unfound_words)))
    unfound_words = sorted(unfound_words)

    # unfound_words = sorted(list(unfound_words))
    count = 0
    for word in unfound_words:
        log_file.write("{0:13s}".format(word))
        count += 1
        while count >= 5:
            count = 0
            log_file.writelines("\n")
