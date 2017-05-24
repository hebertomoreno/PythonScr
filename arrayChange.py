def arrayChange(inputArray):
	cont = 0
	newArray = []
	previousNumber = inputArray[0]
	newArray.append(previousNumber)
	for number in inputArray[1:]:
		if number < previousNumber:
			print("Less Than")
			print("PrevNum: ",previousNumber)
			print("Number: ", number)
			cont += (previousNumber - number) +1 
			number += (previousNumber - number) +1 
		elif number == previousNumber:
			print("Equal")
			print("PrevNum: ",previousNumber)
			print("Number: ", number)
			number +=1 
			cont += 1 
		newArray.append(number)
		previousNumber = number
		print(newArray)
	return cont

print(arrayChange([2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15]))

