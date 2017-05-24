def avoidObstacles(inputArray):
    inputArray = sorted(inputArray)
    divFlag = 0
    for i in range(1,20):
        for number in inputArray:
            if(number % i == 0):
                divFlag += 1
        if divFlag == 0:
            return i
        divFlag = 0