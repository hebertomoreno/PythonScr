n = int(input())

birds = list(map(int,input().split()))

print (max(set(birds), key=birds.count))
