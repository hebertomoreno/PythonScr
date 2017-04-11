maxWeight = float(input())
numberOfBoxes = float(input())
meanWeight = float(input())
stdDev = float(input())

import math

def lessThan(x, mean, stdDev):
	result = 0.5 * (1 + math.erf((x-mean) / (stdDev * math.sqrt(2))))

	return round(result,4)

print (lessThan(maxWeight, numberOfBoxes * meanWeight, math.sqrt(numberOfBoxes) * stdDev))