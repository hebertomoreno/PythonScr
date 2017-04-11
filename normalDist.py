import math

mean, stdDev = [float(x) for x in input().split()]
firstX = float(input())
lowX, highX = [float(x) for x in input().split()]

def lessThan(x, mean, stdDev):
	result = 0.5 * (1 + math.erf((x-mean) / (stdDev * math.sqrt(2))))

	return round(result, 3)

def betweenThisAndThat(x_low, x_high, mean, std):
	low = 0.5 * (1 + math.erf((x_low-mean) / (stdDev * math.sqrt(2))))
	high = 0.5 * (1 + math.erf((x_high-mean) / (stdDev * math.sqrt(2))))
	result = high-low
	return round(result, 3)

print(lessThan(firstX, mean, stdDev))
print(betweenThisAndThat(lowX, highX, mean, stdDev))
