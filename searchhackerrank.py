import re

startswith = re.compile(r'^(hackerrank)\w*')
endswith = re.compile(r'\w*hackerrank$')
somewhere = re.compile(r'\w*hackerrank\w*')

n = int(input())

for i in range(n):
	word = input()
	if(re.search(startswith, word) and re.search(endswith,word)):
		print("0")
	elif(re.search(startswith,word)):
		print("1")
	elif(re.search(endswith,word)):
		print("2")
	else:
		print("-1")
