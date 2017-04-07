n = int(input())

def intifyList(listToInt):
	intedList = listToInt.split()
	intedList = list(map(int,intedList))

	return intedList

choc = intifyList(input())
d, m = intifyList(input())

start = 0
end = m
count = 0
while end <= len(choc):
	if sum(choc[start:end])==d:
		count+=1 
	start+=1
	end+=1

print(count)
