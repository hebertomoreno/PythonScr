def reverseParentheses(s):
	s = list(s)
	openArr = []
	toPop = []
	for index, ch in enumerate(s):
		if(ch == '('):
			openArr.append(index)
		if(ch == ')'):
			lastPar = openArr.pop()
			print("Last Par: ",str(lastPar))
			print("Index: ",str(index))
			s[lastPar+1:index] = s[index-1:lastPar:-1]
			print(s)
	s = ''.join(s)
	s = s.replace("(","")
	s = s.replace(")","")
	return s


word = input()
print(reverseParentheses(word))
