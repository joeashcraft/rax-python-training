"""Lab 04b.

Read the data in tmpprecip2012.dat and create a two-dimensional list containing
all the data that will allow you to print a report by month of the following:
*   Average high temperature,
*   Maximum high temperature,
*   Minimum high temperature

Once that works, try your program on tmpprecip.dat. It contains over 100 years
of daily data.
"""

file = open("./Python II Data/tmpprecip.dat", 'r')
# file = open("./tmpprecip2012_head.dat", 'r')
# data = file.read()

# months list
months = []
for i in range(13):
    # [ hi temp, lo temp, total temps, day count ]
    months.append([0, 999, 0, 0])

for line in file:
    try:
        month = int(line[0:2])
        # day   = int(line[2:4])
        # year  = int(line[4:8])
        # precip = float(line[8:13])
        hi_temp = int(line[13:])
    except ValueError:
        continue

    # if this line has a higher temp than stored hi temp, replace
    if hi_temp > months[month][0]:
        months[month][0] = hi_temp

    # if this line has a lower temp than stored lo temp, replace
    if hi_temp < months[month][1]:
        months[month][1] = hi_temp

    months[month][2] += hi_temp  # running total of temps for later avg

    months[month][3] += 1  # count the days

for i in range(1, 13):
    # month number
    print '{:2d}'.format(i),
    # avg high temp
    print '{:3.1f}'.format(float(months[i][2])/months[i][3]),
    # max high temp
    print '{:3d}'.format(months[i][0]),
    # min high temp
    print '{:3d}'.format(months[i][1])

file.close()
