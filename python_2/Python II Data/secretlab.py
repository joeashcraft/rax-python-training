

import urllib
conn = urllib.urlopen('http://thinkpython.com/secret.html')
print conn
for line in conn:
    print line.strip()
