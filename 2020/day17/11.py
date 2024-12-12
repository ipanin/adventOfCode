from collections import *
from functools import lru_cache
import heapq
import itertools
import math
import random
import sys
import util


def h(grid):
    return "".join(["".join("".join(row) for row in slice) for slice in grid])


def step1(grid):
    nxt = [['.' for _ in row] for row in grid]

    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            ct = Counter(grid[i + dx][j + dy] for dx in range(-1, 2) for dy in range(-1, 2) if 0 <= i + dx < len(grid) and 0 <= j + dy < len(grid[i]) and (dx, dy) != (0, 0))
            if c == 'L' and ct['#'] == 0:
                nxt[i][j] = '#'
            elif c == '#' and ct['#'] >= 4:
                nxt[i][j] = 'L'
            else:
                nxt[i][j] = grid[i][j]
    return nxt


def step2(grid):
    GZ, GY, GX = len(grid), len(grid[0]), len(grid[0][0])
    NZ, NY, NX = GZ+2, GY+2, GX+2
    
    nxt = []
    for z in range(NZ):
        slic = []
        for y in range(NY):
            slic.append(['.'] * NX)
        nxt.append(slic)
                
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
                            if (dx, dy, dz) == (0, 0, 0):
                                continue
                            nx = gx + dx
                            ny = gy + dy
                            nz = gz + dz
                            if 0 <= nx < GX and 0 <= ny < GY and 0 <= nz < GZ:
                                active += grid[nz][ny][nx] == '#'
                val = '.'
                if 0 <= gx < GX and 0 <= gy < GY and 0 <= gz < GZ:
                    val = grid[gz][gy][gx]

                if val == '#' and active in [2,3]:
                    nxt[z][y][x] = '#'
                elif val == '.' and active == 3:
                    nxt[z][y][x] = '#'
                #else:
                #    nxt[z][y][x] = '.'

    return nxt


def main():
    grid = []
    grid.append(util.load_matrix("input.txt"))

    #while True:
    for i in range(6):
        nxt = step2(grid)
        if h(nxt) == h(grid):
            break
        grid = nxt

    print(h(grid).count("#"))


if __name__ == "__main__":
    main()
