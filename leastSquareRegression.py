mathScores = []
statScores = []
n = 5
for i in range(5):
	mathScore, statScore = list(map(float, input().split()))
	mathScores.append(mathScore)
	statScores.append(statScore)

sumMathScores = sum(mathScores)
sumStatScores = sum(statScores)

avgMathScores = sumMathScores/n
avgStatScores = sumStatScores/n

sumOfMathSquares = sum([i**2 for i in mathScores])

sumOfXY = sum([i*j for i, j in zip(mathScores, statScores)])

b = (n*(sumOfXY)-sumMathScores*sumStatScores)/(n*sumOfMathSquares-sumMathScores**2)

a = avgStatScores - b*avgMathScores

y = a + b * 80

print(round(y, 3))