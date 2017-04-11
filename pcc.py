#Pearson Correlation Coefficient
#Receives two lists of numbers and calculates the PCC
import math
n = int(input())

xNumbers = list(map(float, input().split()))
yNumbers = list(map(float, input().split()))

def calcMean(numbers):
	return sum(numbers)/len(numbers)

def calcStdDev(mean,numbers):
	numArray = []
	for number in numbers:
		numArray.append((number-mean)**2)
	return math.sqrt(calcMean(numArray))

xMean = calcMean(xNumbers)
yMean = calcMean(yNumbers)
xStd = calcStdDev(xMean, xNumbers)
yStd = calcStdDev(yMean, yNumbers)

topSum = 0
for numberx, numbery in zip(xNumbers, yNumbers):
	topSum += (numberx - xMean) * (numbery-yMean)

result = topSum/(n * xStd * yStd)

print(round(result,3))
