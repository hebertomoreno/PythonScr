n = int(input())

def intifyList(listToInt):
	intedList = listToInt.split()
	intedList = list(map(int,intedList))

	return intedList

years = intifyList(input())
minLoss = 100000000000

for index, year in enumerate(years):
	for year2 in years[index+1:]:
		loss = year - year2
		if(loss<minLoss and loss>0):
			minLoss = loss
print (minLoss)