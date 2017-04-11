from math import exp
average = float(input())
expected = float(input())

def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def poisson(y, k):

	top = (y**k) * exp(-y)
	bottom = fact(k)
	
	return top/bottom

print(round(poisson(average, expected),3))