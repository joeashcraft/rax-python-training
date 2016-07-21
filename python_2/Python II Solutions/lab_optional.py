"""lab_optional.py

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
"""

# fin = open('/home/student/pydata/tmpprecip.dat')
fin = open('c:/pydata/tmpprecip.dat')
yrdic = {}
mondic = {}

# yrdic format: key: year; value: list[precip, maxhi, minhi, tottemp, daycnt]
# mondic format: key: month(2 digit); total precip

for linein in fin:
    tyr = linein[4:8]
    tmon = linein[0:2]
    if not (tyr.isdigit()and tmon.isdigit()):
        print 'Bad Data - {0!r}'.format(linein)
#        print 'Bad Data - %r' % (linein)  # Older formatting
        continue    
    try:
        precip = float(linein[8:13])
        temp = int(linein[13:16])
        
    except ValueError:
        print 'Bad Data - {0!r}'.format(linein)
#        print 'Bad Data - %r' % (linein)  # Older formatting
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

print 'Year  Rain Max Hi Min Hi Avg Hi'
for i in lst:
    avgtmp = float(i[4])/i[5]
#    print '%s  %4.1f  %4d %5d %7.1f' % (
#        i[0], i[1], i[2], i[3], avgtmp)  # Older formatting
    print '{0}  {1:4.1f}  {2:4d} {3:5d} {4:7.1f}'.format(
        i[0], i[1], i[2], i[3], avgtmp)  

monlst = mondic.items()
monlst.sort()
print '\n\n'
for i in monlst:
    print '{0} {1:5.2f}'.format(i[0], i[1]/len(lst))
#    print '%s %5.2f' % (i[0], i[1]/len(lst))  # Older formatting
               
fin.close()
        
