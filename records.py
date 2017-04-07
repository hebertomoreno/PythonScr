n = int(input())

def intifyList(listToInt):
	intedList = listToInt.split()
	intedList = list(map(int,intedList))

	return intedList

games = intifyList(input())

highestScore, lowestScore = games[0]
recCount, lowCount = 0
for game in games:
	if(game > highestScore):
		highestScore = game
		recCount += 1
	elif(game < lowestScore):
		lowestScore = game
		lowCount += 1
print(recCount, lowCount)