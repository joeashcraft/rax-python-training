"""lab_02a_letters2.py

This program evaluates all of the alphabetic characters in the book,
"Alice in Wonderland."  It counts all of the alphabetic characters as
well as the number of e's used.  It then prints the total number of
letters, the total number of e's and the percent of the total that
are e's.  The difference here is that string methods are used where
applicable.
"""

tot_letters = 0
tot_e = 0

fin = open('/home/student/pydata/alice_in_wonderland.dat')  # Linux
# fin = open('c:/pydata/alice_in_wonderland.dat')  # Windows
bookin = fin.read()
for i in bookin:
    if i.isalpha():
        tot_letters += 1
        if i.lower() == 'e':
            tot_e += 1
print('Total letters: {0:,d}'.format(tot_letters))
print('Total e\'s: {0:,d}'.format(tot_e))
print('{0:.1%} of all the letters are e\'s'.format(
        float(tot_e)/tot_letters))
fin.close()
