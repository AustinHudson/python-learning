import pylab

def producePlot(lowTemps, highTemps):
    assert len(lowTemps) == len(highTemps)
    diffTemps = []
    for i in range(len(lowTemps)):
        diffTemps.append(int(highTemps[i]) - int(lowTemps[i]))
    pylab.figure(1)
    pylab.plot(range(1, 32), diffTemps)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.show()

def plotAvgTemps(lowTemps, highTemps):
    assert len(lowTemps) == len(highTemps)
    avgTemps = []
    for i in range(len(lowTemps)):
        avgTemp = (int(highTemps[i]) + int(lowTemps[i])) / 2.
        avgTemps.append(avgTemp)
    pylab.figure(1)
    pylab.plot(range(1, 32), avgTemps)
    pylab.title('Average Day Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Average Temperature')
    pylab.show()

inFile = open('julyTemps.txt')

lowTemps = []
highTemps = []

for line in inFile.readlines():
    fields = line.split()
    if len(fields) == 3 and fields[0].isdigit():
        lowTemps.append(fields[2])
        highTemps.append(fields[1])

#producePlot(lowTemps, highTemps)
plotAvgTemps(lowTemps, highTemps)
