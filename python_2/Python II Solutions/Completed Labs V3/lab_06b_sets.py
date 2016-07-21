"""lab_06b_sets.py

This program creates two sets from the contents of two files by
nesting an open within a list function which is within a set
function.  While this level of nesting is not recommended, it's
good to know it actually works.

The servers set contains a master list of servers to be updated.
The updates set contains the latest set of servers that have been
updated.  The update items are submitted manually by the admin
responsible for the server.  Sometimes, they are not accurate.
"""

# updates = set(list(open('c:/pydata/serverupdates.txt', 'r')))
# servers = set(list(open('c:/pydata/servers.txt', 'r')))
updates = set(list(open('/home/student/pydata/serverupdates.txt', 'r')))
servers = set(list(open('/home/student/pydata/servers.txt', 'r')))

if updates.issubset(servers):  # one way to test
    print('All updates found in master list')
else:
    print('Some updates not found in the master list')
    
if updates <= servers:  # another way to do the same test
    print('All updates found in master list')
else:
    print('Some updates not found in the master list')

# One way to isolate the unmatched servers
diff = updates.difference(servers) 
if len(diff) > 0:
    print(len(diff), 'server updates not found')
    for server_name in diff:
        print(server_name, end=' ')

# Another way to isolate the same unmatched servers
diff = updates - servers  
if len(diff) > 0:
    print(len(diff), 'server updates not found')
    for server_name in diff:
        print(server_name, end=' ')

fout = open('/home/student/newmaster.txt', 'w')
# fout = open('c:/pydata/newmaster.txt', 'w')
newset = servers.difference(updates) # or newset = servers - updates
print('Original servers', len(servers), '\nValid updates', len(
    updates) - len(diff), '\nNew servers', len(newset))
fout.writelines(newset)
fout.close()
