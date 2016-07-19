"""lab 02a.

count alpha characters and 'e' in text of Alice in Wonderland.
"""

alpha_count, e_count = 0.0, 0.0

file = open("./Python II Data/alice_in_wonderland.dat", 'r')
data = file.read()
file.close()

for character in data:
    if character.isalpha():
        alpha_count += 1
        if character.lower() == 'e':
            e_count += 1

print "%-27s %9d" % ("Count of alpha characters:", alpha_count)
print "%-27s %9d" % ("Count of 'e':", e_count)
print "%-27s %9.1f%%" % ("Percent of 'e' in total:", e_count/alpha_count*100.0)
