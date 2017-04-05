import sys

n = int(input().strip())

def staircase(steps):
	for i in range(1,steps+1):
		for j in range(steps-i):
			print(" ",end="")
		#Print hashtags
		for j in range(i):
			print("#",end="")
		print("")
staircase(n)