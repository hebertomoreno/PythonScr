def digit_root(n): 
    return (n - 1) % 9 + 1 if n else 0

def digitRootSort(a):
    for number in a:
        for i in range(len(a)-1):
            if(digit_root(a[i]) > digit_root(a[i+1])):
                temp = a[i+1]
                a[i+1] = a[i]
                a[i] = temp
            elif(digit_root(a[i]) == digit_root(a[i+1])):
                if(a[i] > a[i+1]):
                    temp = a[i+1]
                    a[i+1] = a[i]
                    a[i] = temp
    return a

numbers = list(map(int, input().split()))

dRoots = []
for number in digitRootSort(numbers):
    dRoots.append(digit_root(number))

print(digitRootSort(numbers))
print(dRoots)