n, d = list(map(int, input().split()))

numbers = list(map(int, input().split()))
i=0
while i<d:
	firstNumber = numbers[0]
	for index, number in enumerate(numbers):
		if index != 0:
			numbers[index-1] = number
	numbers.pop(-1)
	numbers.append(firstNumber)
	i+=1
for number in numbers:
	print(number, end=" ")