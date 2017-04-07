n,h = input().split(" ")

n = int(n)
h = int(h)

def intifyList(listToInt):
	intedList = listToInt.split()
	intedList = list(map(int,intedList))

	return intedList

hurdles = intifyList(input())

potions = 0

for hurdle in hurdles:
	if(hurdle > h):
		potions += hurdle - h
		h = h + (hurdle-h)

print(potions)
