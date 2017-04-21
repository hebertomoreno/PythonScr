n = int(input())
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def f7(seq):
	seen = set()
	seen_add = seen.add
	return [x for x in seq if not (x in seen or seen_add(x))]

def find(l, elem):
	for row, i in enumerate(l):
		try:
			column = i.index(elem)
		except ValueError:
			continue
		return row, column
	return -1

for i in range(n):
	#Input the word
	keyWord = input()
	#Convert to All Caps
	keyWord = keyWord.upper()
	#Append the alphabet to the keyword
	newAlphabet= keyWord + alphabet
	#Removes duplicates from the alphabet, but keeps the order. 
	newAlphabet = f7(newAlphabet)
	#Strip the duplicates from the keyword
	keyWord = f7(keyWord)
	#Make a new variable to hold the keyword sorted alphabetically
	orderedKeyWord = sorted(keyWord)

	#Fill an array with the position of the original characters in the 
	#sorted array.
	cypherNumbers = []
	for letter in orderedKeyWord:
		cypherNumbers.append(keyWord.index(letter))
	cypherArray = []
	newArray = []

	#Fill the cypherArray with the letters in the alphabet taking into
	#account the size of the word. 
	alphArray = []
	cont= 1
	for letter in newAlphabet:
		if(cont==len(keyWord)):
			alphArray.append(letter)
			cypherArray.append(alphArray)
			alphArray=[]
			cont=1
		#If this is the last letter in the array, append it to 
		# a chunk and fill the rest with zeroes. The Zeroes will not
		#be taken into account in future manipulations of the array. 
		#This is to avoid empty index exceptions. 
		elif(letter==newAlphabet[-1]):
			alphArray.append(letter)
			while(cont != len(keyWord)):
				alphArray.append("0")
				cont+=1
			cypherArray.append(alphArray)
		else:
			alphArray.append(letter)
			cont +=1
	#
	encryptedArray = []
	for number in cypherNumbers:
		chunkArray=[]
		for row in cypherArray:
			chunkArray.append(row[number])
		encryptedArray.append(chunkArray)

	#Flatten the encrypted Array
	flatArray = []
	for row in encryptedArray:
		for element in row:
			if(element != '0'):
				flatArray.append(element)

	#Parse the string with the arrays
	superString = input()
	for letter in superString:
		if(letter == " "):
			print(" ", end="")
		else:
			location = flatArray.index(letter)
			newLetter = alphabet[location]
			print(newLetter, end="")
	print("")