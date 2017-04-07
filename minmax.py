def intifyList(listToInt):
	intedList = listToInt.split()
	intedList = list(map(int,intedList))

	return intedList

numbers = intifyList(input())
minimum = 100000000000
maximum = 0
for index, number in enumerate(numbers):
	tempSum = 0
	for index2, number2 in enumerate(numbers):
		if(index2 != index):
			tempSum += number2
	if(tempSum>maximum):
		maximum = tempSum
	if(tempSum<minimum):
		minimum = tempSum

print(minimum, maximum)