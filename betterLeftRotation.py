n, k = list(map(int, input().split()))

numbers = list(map(int,input().split()))

answer = numbers[k:]+numbers[:k]

for number in answer:
	print(number, end=" ")