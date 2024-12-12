def step(grid):
    for p in grid: grid[p] += 1
    res = 0
    while (flashes := sum(flash(grid, p) for p,v in grid.items() if v > 9)):
        res += flashes
    return res

def flash(grid, p):
    grid[p] = 0
    for d in [-1, 1, -1j, 1j, -1-1j, -1+1j, 1+1j, 1-1j]:
        p2 = p + d
        if p2 in grid and grid[p2] > 0:
            grid[p2] += 1                   
    return 1

grid = {x+y*1j: int(c) for x,line in enumerate(open('input.txt'))
                            for y,c in enumerate(line.strip())}
nStep = 100
print("Part 1:", sum(step(grid) for _ in range(nStep)))

while step(grid) != 100: nStep += 1
print("Part 2:", nStep+1)
