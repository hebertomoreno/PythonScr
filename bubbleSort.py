from random import randint

n = int(input())
#numbers = list(map(int, input().split()))
numbers = []
for i in range(n):
	numbers.append(randint(0,1000000)0)
print("Random Array Created...")
numSwaps = 0
numCycles = 0
print("Sorting Array...")
for number in numbers: 
	numSwapsPerformed = 0
	for i in range(n-1):
		if(numbers[i] > numbers[i+1]):
			_ = numbers[i+1]
			numbers[i+1] = numbers[i]
			numbers[i] = _
			numSwaps += 1
			numSwapsPerformed += 1
		numCycles += 1
	if(numSwapsPerformed==0):
		print("Array is in order.")
		break
print("Performed "+str(numCycles)+" cycles.")
print("Array is sorted in "+str(numSwaps)+" swaps.")
print("First Element: ",str(numbers[0]))
print("Last Element: ", str(numbers[-1]))
#print(numbers)