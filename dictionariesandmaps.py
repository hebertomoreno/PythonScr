n = int(input())

phoneDict = {}

for i in range(n):
	name, phone = list(input().split())
	phoneDict[name] = phone

while True: 
	try: 
		nameToLook = input()
		if nameToLook in phoneDict:
			print(nameToLook + "=" + phoneDict[nameToLook])
		else:
			print('Not found')
	except: 
		break
