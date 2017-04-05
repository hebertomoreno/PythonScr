n = int(input())

def intifyList(listToInt):
	intedList = listToInt.split()
	intedList = list(map(int,intedList))

	return intedList

numberList = intifyList(input())
weightList = intifyList(input())
topNum = 0
botNum = 0
for num, wei in zip(numberList, weightList):
	topNum += (num*wei)
	botNum += wei

weiMean = topNum/botNum
print(round(weiMean,1))
