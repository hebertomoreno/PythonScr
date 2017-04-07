n = int(input())

for i in range(n):
	catA, catB, mouseC = input().split(" ")

	catA = int(catA)
	catB = int(catB)
	mouseC = int(mouseC)

	if(abs(catA-mouseC) == abs(catB-mouseC)):
		print("Mouse C")
	elif(abs(catA-mouseC)> abs(catB-mouseC)):
		print("Cat B")
	else:
		print("Cat A")