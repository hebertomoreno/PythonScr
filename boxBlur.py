import math
newArray = []
columnCounter = 0
while columnCounter <len(image)-2:
	rowArray = []
	horizontalInit = 0
	verticalInit = 0
	while horizontalInit < len(image[0]):
		expectedAverage = 0
		for i in range(columnCounter,columnCounter+3):
			if((verticalInit+3)<=len(image[0])):
				for j in range(verticalInit,verticalInit+3):
					expectedAverage += image[i][j]
		if(math.floor(expectedAverage/9) != 0):
			rowArray.append(math.floor(expectedAverage/9))
		horizontalInit += 1
		verticalInit+=1
	newArray.append(rowArray)
	columnCounter += 1
print("NEW ARRAY: ",newArray)