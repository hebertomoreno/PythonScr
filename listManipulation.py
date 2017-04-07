n = int(input())

newList = []

for i in range(n):
	comList = input().split()

	command = comList[0]

	if(command == "insert"):
		comList[1] = int(comList[1])
		comList[2] = int(comList[2])
		newList.insert(comList[1], comList[2])
	if(command == "print"):
		print(newList)
	if(command == "remove"):
		print(comList[1])
		newList.pop(comList[1])
	if(command == "append"):
		newList.append(comList[1])
	if(command == "sort"):
		newList.sort()
	if(command == "pop"):
		newList.pop()
	if(command == "reverse"):
		newList.reverse()

