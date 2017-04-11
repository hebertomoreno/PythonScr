s, t = list(map(int, input().split()))
a, b = list(map(int, input().split()))
appleQuant, orangeQuant = list(map(int, input().split()))
appleDist = list(map(int, input().split()))
orangeDist = list(map(int, input().split()))
cont = 0
for apple in appleDist:
	aPosition = a + apple
	if(aPosition>=s and aPosition<=t):
		cont += 1
print(cont)
cont = 0
for orange in orangeDist:
	oPosition = b + orange
	if(oPosition>=s and oPosition<=t):
		cont += 1
print(cont)