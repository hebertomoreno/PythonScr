import re

idRegex = re.compile(r'''
	^[a-z]{0,3}
	[0-9]{2,8}
	[A-Z]{3,}$''')

n = int(input())

for i in range(n):
	word = input()
	if(re.search(idRegex, word)):
		print("VALID")
	else:
		print("INVALID")
