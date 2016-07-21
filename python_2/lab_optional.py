"""Optional Lab.

Read the tmpprecip.dat file and use a dictionary to accumulate the data
necessary to report the following for each year:
  * Total rainfall (precipitation)
  * Maximum high temperature
  * Minimum high temperature
  * Average high temperature

Use a separate dictionary to report the average rainfall by month.

Create well-formatted reports from each dictionary.
The format of the data is the same as it was in Lab 2b. The data goes
from 1/1/1900 to 12/31/2012.
"""

# file = open("./Python II Data/tmpprecip2012.dat", 'r')  # short file for testing
file = open("./Python II Data/tmpprecip.dat", 'r')  # data for years 1900/2012

yearly_data = {}  # { 2012: [sum_precip, max_temp, min_temp, sum_temp, count_days ], 1: ... }
monthly_data = {}  # { 0: [], 1: [sum_precip, count_days], ... }

for line in file:
    try:
        month = int(line[0:2])
        # day = int(line[2:4])
        year = int(line[4:8])
        precip = float(line[8:13])
        hi_temp = int(line[13:])
    except:
        continue
    # print year, precip

    if year not in yearly_data:
        # year does not exist, then initialize
        yearly_data[year] = [0.0, 0.0, 999.0, 0.0, 0]

    yearly_data[year][0] += precip  # sum_precip

    if hi_temp > yearly_data[year][1]:
        yearly_data[year][1] = hi_temp  # max_temp

    if hi_temp < yearly_data[year][2]:
        yearly_data[year][2] = hi_temp  # min_temp

    yearly_data[year][3] += hi_temp  # sum_temp

    yearly_data[year][4] += 1  # count_days

    if month not in monthly_data:
        # month does not exist, then initialize
        monthly_data[month] = 0

    monthly_data[month] += precip  # sum_precip

# report the following for each year:
#   * Total rainfall (precipitation)
#   * Maximum high temperature
#   * Minimum high temperature
#   * Average high temperature

year_lst = []
for i in yearly_data:
    # create list to sort later
    year_lst.append([
        i,
        yearly_data[i][0],  # sum_precip
        yearly_data[i][1],  # max_temp
        yearly_data[i][2],  # min_temp
        yearly_data[i][3]/yearly_data[i][4]   # avg temp
    ])
year_lst.sort()

print "{} {} {} {} {}".format(
    "Year",
    "Total Rainfall",
    "Max Hi",
    "Min Hi",
    "Avg Hi"
)
# print "{0:4s} {1:14.1f} {2:6d} {3:6d} {4:6.1f}".format()
for i in year_lst:
    print "{:4d} {:14.1f} {:6.0f} {:6.0f} {:6.0f}".format(
        i[0],
        i[1],
        i[2],
        i[3],
        i[4]
    )

# report the average rainfall by month.
print "{:s}    {:s}".format("Month", "Avg Rainfall")
for month, sum_precip in monthly_data.items():
    print "{0:5d}    {1:12.1f}".format(
        month,  # key == month number
        sum_precip/len(yearly_data.keys())  # avg monthly rainfall
    )
