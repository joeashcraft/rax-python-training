"""lab_optional_runavg.py

This program reads the temperature/precipitation data for San Antonio
for the period 1/1/1900 to 12/31/2012.  It accumulates the data in two
dictionaries; one by year and the other by month.  The yearly dictionary
is used to produce a report showing, by year, the total precipitation,
the higest high temperature, the lowest high temperature, the aggregate
temperatures and the number of days for which data was collected.  The
latter two items are used to calculate the average high temperature for
the year.  The monthly dictionary is used to accumulate, by month, the
aggregate precipitation.  The average precipitation for each month is
calculated by dividing the aggregate precipitation by the number of
years in the sample.
This version of the program also produces a 20-year moving average.
"""

# fin = open('/home/student/pydata/tmpprecip.dat', 'r')
fin = open('c:/pydata/tmpprecip.dat', 'r')
yrdic = {}
mondic = {}

# yrdic format: key: year; value: list[precip, maxhi, minhi, tottemp, daycnt]
# mondic format: key: month(2 digit); total precip

for linein in fin:
    tyr = linein[4:8]
    tmon = linein[0:2]
    if not (tyr.isdigit()and tmon.isdigit()):
        print 'Bad Data - {0!r}'.format(linein)
        continue    
    try:
        precip = float(linein[8:13])
        temp = int(linein[13:16])
        
    except ValueError:
        print 'Bad Data - {0!r}'.format(linein)
        continue
    if tyr in yrdic:
        yrdic[tyr][0] += precip
        if yrdic[tyr][1] < temp:
            yrdic[tyr][1] = temp
        if yrdic[tyr][2] > temp:
            yrdic[tyr][2] = temp
        yrdic[tyr][3] += temp
        yrdic[tyr][4] += 1
    else:
        yrdic[tyr] = [precip, temp, temp, temp, 1]

    if tmon in mondic:
        mondic[tmon] += precip
    else:
        mondic[tmon] = precip

lst = []
for i in yrdic:
    lst.append([i, yrdic[i][0], yrdic[i][1], yrdic[i][2],   
                yrdic[i][3], yrdic[i][4]])
lst.sort()

ralst = []
print 'Year Rain R Avg Max Hi Min Hi Avg Hi'
for i in lst:
    ralst.append(i[1])
    if len(ralst) < 21: # Keep track of the last 20 years of precip
        ra = 0.0
    else:
        ralst.pop(0) # Make sure you keep only the most recent 20 yrs
        ra = float(sum(ralst))/len(ralst) # Calc the 20-year average
    avgtmp = float(i[4])/i[5]
    print '{0}  {1:4.1f}  {2:4.1f}  {3:4d} {4:5d} {5:7.1f}'.format(
        i[0], i[1], ra, i[2], i[3], avgtmp)

monlst = mondic.items()
monlst.sort()
print '\n\n'
for i in monlst:
    print '{0} {1:5.2f}'.format(i[0], i[1]/len(lst))
               
fin.close()
        
