from math import sqrt
n = int(input())

def intifyList(listToInt):
	intedList = listToInt.split()
	intedList = list(map(int,intedList))

	return intedList

numberList = intifyList(input())
def getStdDev(numList):
	n = len(numList)
	theMean = getMean(numList)
	stdDev = 0
	for number in numList:
		disty = number-theMean
		disty = disty*disty
		stdDev += disty
	stdDev = stdDev/n
	stdDev = sqrt(stdDev)
	return(round(stdDev,1))

def getMean(numList):
    meanVar = 0
    for number in numList:
        meanVar = meanVar + number
    meanVar = round(meanVar/n,1)
    return meanVar

print(getStdDev(numberList))