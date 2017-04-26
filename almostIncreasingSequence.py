def almostIncreasingSequence(sequence):
	for index,number in enumerate(sequence):
		flag = 0
		tempArr = sequence[:index]+sequence[index+1:]
		print(tempArr)
		for i in range(len(tempArr)-1):
			if(tempArr[i] >= tempArr[i+1]):
				flag = 1
				break
		if(flag == 0):
			return True
	return True

numbers = list(map(int, input().split()))

print(almostIncreasingSequence(numbers))