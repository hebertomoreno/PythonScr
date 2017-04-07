def displayPathToPrincess(n, grid):
    for idx, row in enumerate(grid):
        if 'p' in row:
            princess = (idx, row.index('p'))
        if 'm' in row:
            mario = (idx, row.index('m'))
    drows = princess[0] - mario[0]
    dcols = princess[1] - mario[1]
    if drows < 0:
        return 'UP\n'
    return 'UP\n' * abs(drows) if drows < 0 else 'DOWN\n' * drows,'LEFT\n' * abs(dcols) if dcols < 0 else 'RIGHT\n' * dcols

m = int(input())
grid = []

for i in range(0, m):
    grid.append(input().strip())

print (displayPathToPrincess(m, grid))