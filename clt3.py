import math

n= float(input())
meanPop = float(input())
stdDev = float(input())
distPercentage = float(input())
z = float(input())

marginOfError = z * stdDev / math.sqrt(n)

print(round(meanPop - marginOfError, 3))
print(round(meanPop + marginOfError, 3))