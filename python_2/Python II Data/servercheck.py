"""
This program creates two sets from the contents of two files by
nesting an open within a list function which is within a set
function.  While this level of nesting is not recommended, it's
good to know it actually works.

The servers set contains a master list of servers to be updated.
The updates set contains the latest set of servers that have been
updated.  The update items are submitted manually by the admin
responsible for the server.  Sometimes, they are not accurate.
"""

updates = set(list(open('c:/pydata/serverupdates.txt', 'r')))
servers = set(list(open('c:/pydata/servers.txt', 'r')))
# updates = set(list(open('/home/student/serverupdates.txt', 'r')))
# servers = set(list(open('/home/student/servers.txt', 'r')))


