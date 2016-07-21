"""lab_02d_findcount.py

This program evaluates all of the words in the book,
"Alice in Wonderland."  It determines how many of the words are
"caterpillar" and how many are "gryphon."  Then it prints the location
of the first occurrence and the last occurrence and the number of
occurrences of both words.
"""

def findcount(book, wrd):
    loc = book.find(wrd)
    loc2 = book.rfind(wrd)
    cnt = book.count(wrd)
    print 'Word is', wrd
    print 'The location of the first occurrence is {0:,d}'.format(loc)
    print 'The location of the last occurrence is {0:,d}'.format(loc2)
    print 'The number of occurrences is {0:,d}'.format(cnt)
    
    """ Older formatting - no thousand separators
    print 'Word is', wrd
    print 'The location of the first occurrence is %d' % (loc)
    print 'The location of the last occurrence is %d' % (loc2)
    print 'The number of occurrences is %d' % (cnt)
    """

# fin = open('/home/student/pydata/alice_in_wonderland.dat')
fin = open('c:/pydata/alice_in_wonderland.dat')
bookin = fin.read()
bookin = bookin.lower()
findcount(bookin, 'caterpillar')
findcount(bookin, 'gryphon')
print "We're done!"
fin.close()


