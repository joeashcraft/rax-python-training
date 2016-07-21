"""Lab 06b.

This program creates two sets from the contents of two files by
nesting an open within a list function which is within a set
function.  While this level of nesting is not recommended, it's
good to know it actually works.

The servers set contains a master list of servers to be updated.
The updates set contains the latest set of servers that have been
updated.  The update items are submitted manually by the admin
responsible for the server.  Sometimes, they are not accurate.

1. Determine whether the list of updates exists in the master
server list. Print a message indicting whether or not this is true.

2. If it is not true (and you know it isn't), create a new set
containing the update items that are NOT in the master server
set. Print the number and names of the unmatched servers.

3. Create a new server set that excludes the valid updates.

4. Print the number of items in the original server set and the new
server set as well as the number of valid updates.

5. Write the contents of the new server set to an external file
using the writelines file method.
"""

# updates = set(list(open('c:/pydata/serverupdates.txt', 'r')))
# servers = set(list(open('c:/pydata/servers.txt', 'r')))
updates = set(list(open('./Python II Data/serverupdates.txt', 'r')))
servers = set(list(open('./Python II Data/servers.txt', 'r')))


# 1. Determine whether the list of updates exists in the master
# server list. Print a message indicting whether or not this is true.

if updates.issubset(servers):
    print "The list of updates exists in the master server list."
else:
    print "The list of updates contains bad names."

# 2. Create a new set containing the update items that are NOT in the master
# server set. Print the number and names of the unmatched servers.
updates_not_in_master = set(updates.difference(servers))
print "{} names found in UPDATES which are not in SERVERS".format(
    len(updates_not_in_master))
for x in updates_not_in_master:
    print x

# 3. Create a new server set that excludes the valid updates.
servers_not_updated = set(servers.difference(updates))
# for x in servers_not_updated:
#     print x

# 4. Print the number of items in the original server set and the new
# server set as well as the number of valid updates.
print "{} in original server list".format(len(servers))
print "{} servers not updated".format(len(servers_not_updated))
print "{} servers updated".format(len(servers.intersection(updates)))

# 5. Write the contents of the new server set to an external file
# using the writelines file method.
try:
    open('./report.txt', 'w').writelines(servers_not_updated)
    print "wrote report.txt with {} lines".format(len(servers_not_updated))
except:
    print "failed to write file report.txt"
