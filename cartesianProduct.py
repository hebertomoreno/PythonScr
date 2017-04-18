setA = list(map(int, input().split()))
setB = list(map(int, input().split()))

cont=0
for i in setA:
	for j in setB:
		print("("+str(i)+","+str(j)+")")
		cont +=1
print(cont)