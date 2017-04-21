def ransom_note(magazine,ransom):
	magSet = set(magazine)
	ranSet = set(magazine)
	for word in ranSet:
		if not word in ranSet:
			return False
	return True
m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")