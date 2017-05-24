iniMatrix = [[True, False, False],
		  [False, True, False],
		  [False, False, False]]
iniMatrix2 = [[True,False,False,True], 
 			  [False,False,True,False], 
 			  [True,True,False,True]]

def addToFringe(row,col,matrix):
	if row-1 >= 0:
		matrix[row-1][col] += 1
	if row-1 >= 0  and col+1<len(matrix[0]):
		matrix[row-1][col+1] += 1
	if col+1 < len(matrix[0]):
		matrix[row][col+1] += 1
	if row+1 < len(matrix) and col+1 < len(matrix[0]):
		matrix[row+1][col+1] += 1
	if row+1 < len(matrix):
		matrix[row+1][col] += 1
	if row+1 < len(matrix) and col-1 >= 0:
		matrix[row+1][col-1] += 1
	if col-1 >= 0:
		matrix[row][col-1] += 1
	if row-1 >= 0 and col-1 >= 0:
		matrix[row-1][col-1] += 1
	return matrix
def generateArray(matrix):
	newArray=[]
	for row in matrix:
		newRow = []
		for element in row:
			newRow.append(0)
		newArray.append(newRow)
	return newArray
def minesweeper(matrix):
	result = generateArray(matrix)
	for indexR,row in enumerate(matrix):
		for indexC,element in enumerate(row): 
			if element:
				result = addToFringe(indexR,indexC,result)
				#for row in result:
					#print(row)
				#print("")
	return result
print(minesweeper(iniMatrix2))