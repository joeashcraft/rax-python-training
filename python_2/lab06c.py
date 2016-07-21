"""Lab 06c.

Change the program you developed in the last lab [06b] to remove the newline
characters from the data you read in.

Then you have to put them back in the data you write. In this case, how will
you read the server data? How will you write the new server file? Be sure to
answer these questions before you write any code.

When finished, you should be able to open the new server file with any text
editor and have it display one server per line.
"""

# updates = set(list(open('c:/pydata/serverupdates.txt', 'r')))
# servers = set(list(open('c:/pydata/servers.txt', 'r')))
updates = open('./Python II Data/serverupdates.txt', 'r')
servers = open('./Python II Data/servers.txt', 'r')

updates = updates.read()
updates = set(updates.splitlines())

servers = servers.read()
servers = set(servers.splitlines())

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
    open('./report.txt', 'w').write('\n'.join(servers_not_updated))
    print "wrote report.txt with {} lines".format(len(servers_not_updated))
except:
    print "failed to write file report.txt"
