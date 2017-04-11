import math

mean, stdDev = [float(x) for x in input().split()]
firstX = float(input())
secondX = float(input())

def lessThan(x, mean, stdDev):
	result = 0.5 * (1 + math.erf((x-mean) / (stdDev * math.sqrt(2))))

	return result

print(round(100 - 100 * lessThan(firstX, mean, stdDev),2))
print(round(100 - 100 * lessThan(secondX, mean, stdDev),2))
print(round(100 * lessThan(secondX, mean, stdDev),2))
