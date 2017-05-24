def arrayMaximalAdjacentDifference(inputArray):
    absMax = 0
    for i in range(0, len(inputArray)-1):
        if( abs( inputArray[i] - inputArray[i+1] ) > absMax):
           absMax = abs(inputArray[i]-inputArray[i+1])
    return absMax

print(arrayMaximalAdjacentDifference([1,3,5,7,9]))