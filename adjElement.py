def adjacentElementsProduct(inputArray):
	largestProduct = -10000000000
	for i in range(len(inputArray) - 1):
		print("Numbers are: "+str(inputArray[i])+' and '+str(inputArray[i+1]))
		print("Product is: "+str(inputArray[i] * inputArray[i+1]))
		if((inputArray[i] * inputArray[i+1]) > largestProduct):
			largestProduct = inputArray[i] * inputArray[i+1]
	return largestProduct

numbers = list(map(int, input().split()))

print(adjacentElementsProduct(numbers))