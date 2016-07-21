
"""lab_08_split_trans.py

This program does the split in the previous lab a different way. It
uses a translate table to replace all punctuation with a space. It
makes use of the maketrans function from the string module to help do
this operation.  While we didn't cover the translate built-in function
in class, this example together with the online documentation should
help you understand how this valuable function is used.
"""

from string import punctuation, maketrans

# fin = open('c:/pydata/split.txt', 'r')
fin = open('/home/student/pydata/split.txt')
txt_in = fin.read().lower()
outtab = len(punctuation) * ' '
transtab = maketrans(punctuation, outtab)
txt_in = txt_in.translate(transtab)
word_lst = txt_in.split()
word_set = set(word_lst)
print('Words in text:', len(word_lst))
print('Unique words in text:', len(word_set))
word_sort = list(word_set)
word_sort.sort()
for entry in word_sort:
    print(entry)

fin.close()
