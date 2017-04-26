def almostIncreasingSequence(sequence):
	for index,number in enumerate(sequence):
		tempArr = sequence[:index]+sequence[index+1:]
		if(tempArr == sorted(set(tempArr))):
			return True
	return False

numbers = list(map(int, input().split()))

print(almostIncreasingSequence(numbers))