n = int(input())

def intifyList(listToInt):
	intedList = listToInt.split()
	intedList = list(map(int,intedList))

	return intedList

cake = intifyList(input())

cake = sorted(cake)

tallestCandle = cake[0]
cont = 0
for candle in cake:
	if(candle > tallestCandle):
		tallestCandle = candle
		cont = 1
	elif(candle == tallestCandle):
		cont += 1

print(cont)