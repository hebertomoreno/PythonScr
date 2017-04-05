n = int(input())

def intifyList(listToInt):
	intedList = listToInt.split()
	intedList = list(map(int,intedList))

	return intedList

numberList = intifyList(input())
freqList = intifyList(input())
finalList = []

for num, freq in zip(numberList, freqList):
	for i in range(0,freq):
		finalList.append(num)
finalList = sorted(finalList)
print("Final List: ", finalList)

def getMedian(numList):
	listLen = len(numList)
	med = 0
	if(listLen%2 == 0):
		med = (numList[listLen//2] + numList[(listLen//2)-1])/2
	else:
		med = numList[(listLen//2)]
	print("This comes from getMedian: ", float(round(med,1)))
	return float(round(med,1))

def getQuartilesDiff(numList):
    med = 0
    n=len(numList)
    print("Final List Len: ",n)
    if(n%2 == 0):
    	halfIndex = (n//2)
    	botHalf = numList[0:halfIndex]
    	topHalf = numList[halfIndex:n]
    	quart1 = getMedian(botHalf)
    	quart3 = getMedian(topHalf)
    	quartDiff = round(quart3-quart1,1)
    	print("Quart 1: ",quart1)
    	print("Quart 3: ",quart3)
    	print("IntQuartRange: ",quartDiff)
    	print(quartDiff)
    else:
    	halfIndex = (n//2)
    	botHalf = numList[0:halfIndex]
    	topHalf = numList[halfIndex+1:n]
    	quart1 = getMedian(botHalf)
    	quart3 = getMedian(topHalf)
    	quartDiff = round(quart3-quart1,1)
    	print("Quart 1: ",quart1)
    	print("Quart 3: ",quart3)
    	print("IntQuartRange: ",quartDiff)
    	print(round(quart3-quart1,1))

getQuartilesDiff(finalList)