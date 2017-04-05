n = int(input())

def intifyList(listToInt):
	intedList = listToInt.split()
	intedList = list(map(int,intedList))

	return intedList

numberList = intifyList(input())

numberList = sorted(numberList)

def getMedian(numList):
	listLen = len(numList)
	med = 0
	if(listLen%2 == 0):
		med = (numList[listLen//2] + numList[(listLen//2)-1])/2
	else:
		med = numList[(listLen//2)]

	return int(round(med))

def getQuartiles():
    med = 0
    n=len(numberList)
    if(n%2 == 0):
    	halfIndex = (n//2)
    	botHalf = numberList[0:halfIndex]
    	topHalf = numberList[halfIndex:n]
    	print(getMedian(botHalf))
    	print(getMedian(numberList))
    	print(getMedian(topHalf))

    else:
    	halfIndex = (n//2)
    	botHalf = numberList[0:halfIndex]
    	topHalf = numberList[halfIndex+1:n]
    	print(getMedian(botHalf))
    	print(numberList[(n//2)])
    	print(getMedian(topHalf))

getQuartiles()