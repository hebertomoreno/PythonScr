def geoDis(n, p):
    q = 1 - p
    return (q**(n-1)) * p

num, den = list(map(float, input().split()))

probabilityOfSuccess = num/den

numberOfTrial = float(input())

print(round(geoDis(numberOfTrial, probabilityOfSuccess),3))