def sortByHeight(a):
	treePositions = []
	people = []
	for index,elem in enumerate(a):
		if(elem == -1):
			treePositions.append(index)
		else: 
			people.append(elem)
	people.sort()
	treePositions.sort()
	people = people[::-1]
	sortedArr = []
	lowLim = 0
	for i in range(len(treePositions)):
		highLim = treePositions[i]
		while lowLim <= highLim:
			if lowLim == highLim:
				sortedArr.append(int("-1"))
				lowLim+=1
			else:
				sortedArr.append(people.pop())
				lowLim+=1
	if(people):
		people = people[::-1]
		for remaining in people: 
			sortedArr.append(remaining)
	return sortedArr

numbers = [-1,150,190,170,-1,-1,160,180]

print(sortByHeight(numbers))