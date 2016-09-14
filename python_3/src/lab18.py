"""Lab 18 - source file.

Using the program you created for Lab 16, separate the code for the
classes from the main program. Place the code for the classes in a
new directory with a short name as directed in PEP 8. Import the
code for the classes from that directory. Keep in mind whether you
want to access the classes through dot notation or not. That will
govern how you do the import.

Use the code on the previous slide to add the new directory to your
path temporarily. Also, add a statement to your main program to
import your class code. Get your program working paying special
attention to the naming requirements. Also, examine the code in
your new directory. Note the module ending with .pyc. We will
discuss this when you are done.
"""

import sys
sys.path.append('/home/student/python-training/python_3/modules')
from bankAccounts import BankAccount, minBankAccount

try:
    a = BankAccount()
except:
    print "FAILED to create 'a'"

try:
    b = minBankAccount(10, 100)
except ValueError, msg:
    print "Failed to create account with minBal; {}".format(msg)
