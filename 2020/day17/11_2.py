import sys
import util


def h(grid):
    return "".join(["".join(["".join("".join(row) for row in slice) for slice in grid3]) for grid3 in grid])

def step2(grid):
    GW, GZ, GY, GX = len(grid), len(grid[0]), len(grid[0][0]), len(grid[0][0][0])
    NW, NZ, NY, NX = GW+2, GZ+2, GY+2, GX+2
    
    nxt = []
    for w in range(NW):
        nxt3 = []
        for z in range(NZ):
            slic = []
            for y in range(NY):
                slic.append(['.'] * NX)
            nxt3.append(slic)
        nxt.append(nxt3)

    for w in range(NW):
        gw = w - 1
        for z in range(NZ):
            gz = z - 1
            for y in range(NY):
                gy = y - 1
                for x in range(NX):
                    gx = x - 1
                    active = 0
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            for dz in range(-1, 2):
                                for dw in range(-1, 2):
                                    if (dx, dy, dz, dw) == (0, 0, 0, 0):
                                        continue
                                    nx = gx + dx
                                    ny = gy + dy
                                    nz = gz + dz
                                    nw = gw + dw
                                    if 0 <= nx < GX and 0 <= ny < GY and 0 <= nz < GZ and 0 <= nw < GW:
                                        active += grid[nw][nz][ny][nx] == '#'
                    val = '.'
                    if 0 <= gx < GX and 0 <= gy < GY and 0 <= gz < GZ and 0 <= gw < GW:
                        val = grid[gw][gz][gy][gx]

                    if val == '#' and active in [2,3]:
                        nxt[w][z][y][x] = '#'
                    elif val == '.' and active == 3:
                        nxt[w][z][y][x] = '#'

    return nxt


def main():
    grid = [[]]
    grid[0].append(util.load_matrix("input.txt"))

    for i in range(6):
        print('.')
        nxt = step2(grid)
        if h(nxt) == h(grid):
            break
        grid = nxt

    print(h(grid).count("#"))


if __name__ == "__main__":
    main()
