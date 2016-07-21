
"""lab_06b_sets.py

This program creates two sets from the contents of two files and
eliminates the newline (\n) character from each entry.  The splitlines
string method is used to accomplish this.  Then, the join method
is used to put the newline back on each entry prior to writing the
new server file.
"""

# Create a set of updates without the newline at the end of each entry
# updatesin = open('c:/pydata/serverupdates.txt', 'r')
updatesin = open('/home/student/pydata/serverupdates.txt', 'r')
tempupdate = updatesin.read()
updates_lst = tempupdate.splitlines()
updates = set(updates_lst)

# Create a set of servers without the newline at the end of each entry
# serversin = open('c:/pydata/servers.txt', 'r')
serversin = open('/home/student/pydata/servers.txt', 'r')
tempserver = serversin.read()
servers_lst = tempserver.splitlines()
servers = set(servers_lst)

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
        print(server_name)

# Another way to isolate the same unmatched servers
diff = updates - servers  
if len(diff) > 0:
    print(len(diff), 'server updates not found')
    for server_name in diff:
        print(server_name)

fout = open('/home/student/newmaster.txt', 'w')
# fout = open('c:/pydata/newmaster.txt', 'w')
newset = servers.difference(updates) # or newset = servers - updates
print('Original servers', len(servers), '\nValid updates', len(
    updates) - len(diff), '\nNew servers', len(newset))
# put the newline character back at the end of each server name.
set_write = '\n'.join(newset)
fout.write(set_write)
fout.close()
