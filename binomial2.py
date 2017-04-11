def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))

def b(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)

l, n = list(map(float, input().split(" ")))

l = l * 0.01

print(round(sum([b(i,n,l) for i in range(0,3)]),3))
print(round(sum([b(i,n,l) for i in range(2,11)]),3))