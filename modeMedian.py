n = int(input())

numberList = input().split()

numberList = list(map(int,numberList))

numberList = sorted(numberList)

def getMean():
    meanVar = 0
    for number in numberList:
        meanVar = meanVar + int(number)
    meanVar = round(meanVar/n,1)
    return meanVar

def getMedian():
    med = 0
    if(n%2 == 0):
        print(numberList[n//2])
        print(numberList[(n//2)-1])
        med = (numberList[n//2] + numberList[(n//2)-1])/2
    else:
        med = numberList[(n//2)+1]
    return round(med,1)

def getMode():
    mode = max(numberList, key = numberList.count)
    return mode

print(getMean())
print(getMedian())
print(getMode())
print(numberList)