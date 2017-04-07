n,k = list(map(int,input().split()))
numberList = list(map(int,input().split()))

cont = 0
for index, number in enumerate(numberList):
	for index2, number2 in enumerate(numberList):
		if(index2!=index):
			if(index<index2 and (number+number2)%k ==0):
				cont +=1

print (cont)