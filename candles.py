n = int(input())

def intifyList(listToInt):
	intedList = listToInt.split()
	intedList = list(map(int,intedList))

	return intedList

numberList = intifyList(input())

numberList = sorted(numberList)

