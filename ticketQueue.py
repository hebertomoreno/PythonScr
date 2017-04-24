n = int(input())
tickets = []
for i in range(n):
	tickets.append(int(input()))
p = int(input())

if(tickets[p] == 1):
	print(len(tickets[:p+1]))
else:
	'''timeInFront = sum([min(tickets[i], tickets[p]) for i in range(p)])
	timeInBack = sum([min(tickets[i],tickets[p]-1)for i in range(p+1,n)])
	print(timeInFront + timeInBack + tickets[p])'''
	print(sum([min(tickets[i], tickets[p]) for i in range(p)])+sum([min(tickets[i],tickets[p]-1)for i in range(p+1,n)])+tickets[p])