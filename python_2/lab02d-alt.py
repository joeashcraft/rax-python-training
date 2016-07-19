"""lab02d-alt.py

In the book, "Alice in Wonderland" find the words caterpillar and gryphon.
Print the location of the first occurrence of each word. Also, print the number
of times each word occurs in the book.

If you finish early, determine the location of the last occurrence of
each word. There is a method that will do this for you.
"""

file = open("./Python II Data/alice_in_wonderland.dat", 'r')
data = file.read()
data = data.lower()
words = ["caterpillar", "gryphon"]

for word in words:
    print "First occurance of %s starts at: %0d" % (word, data.find(word))
    print "Last occurance of %s starts at:  %0d" % (word, data.rfind(word))
    print "%s is found %0d times." % (word, data.count(word))
    print

file.close()
