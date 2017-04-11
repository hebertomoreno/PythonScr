n,k = list(map(int,input().split()))

meals = list(map(int, input().split()))

b = int(input())

annaSum = 0
for index, meal in enumerate(meals):
	if(index != k):
		annaSum += meal
annaSum = annaSum/2

if(b == annaSum):
	print("Bon Appetit")
else:
	print(int(b - annaSum))