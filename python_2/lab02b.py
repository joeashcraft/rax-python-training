"""lab 02b.

count and print number of days with measureable precipitation and
  total precipitation for year
"""

file = open("./Python II Data/tmpprecip2012.dat", 'r')
# file = open("./tmpprecip2012_head.dat", 'r')
# data = file.read()

days_of_precip = 0
total_precip = 0.0

for line in file:
    try:
        # month == int(line[0:2])
        # day   == int(line[2:4])
        # year  == int(line[4:8])
        precip = float(line[8:13])
        # hi_temp == int(line[13:])
    except ValueError:
        continue
    if precip > 0:
        days_of_precip += 1
        total_precip += precip

print "Days with precipitation: %3d" % (days_of_precip)
print "Total Precip for Year: %3f" % (total_precip)

file.close()
