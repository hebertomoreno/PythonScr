n = int(input())

def intifyList(listToInt):
	intedList = listToInt.split()
	intedList = list(map(int,intedList))

	return intedList

numberList = intifyList(input())
numberList.sort()
numberList.reverse()
highest = numberList[0]
for number in numberList:
    if(number < highest):
        print(number)
        break