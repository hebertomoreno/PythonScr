#Recieves the dimensions of the cube and then returns the coordinates in which the sum
#of x, y and z is different from N
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

listOfCubes = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
#listOfCubes = listOfCubes.sort()

print(listOfCubes)