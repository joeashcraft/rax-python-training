"""Lab 17 - sys and os Modules.

You may need to change the values of the
ds and di variables to get a meaningful result.
"""
import os, sys

PATH_TO_TRAINING_DATA = '/home/student/python-training/python_3/'
ds = PATH_TO_TRAINING_DATA + 'Python III Data/words.txt'  # directory with file
di = PATH_TO_TRAINING_DATA + 'Python III Data/'    # directory only
# ds = 'c:/pydata/words.txt'
# di = 'c:/pydata'

print "ds =", ds
print "di =", di

print "ds", "exists" if os.path.exists(ds) else "does not exist"
print "di", "exists" if os.path.exists(di) else "does not exist"

print "First 9 ENV Items".center(60)
for i in range(9):
    print os.environ.items()[i]

sys.exit()
