# Day 11: Dumbo Octopus
# Life-симулятор
# Для работы с матрицей использую словарь комплексных чисел

# There are 100 octopuses arranged neatly in a 10 by 10 grid. Each octopus slowly gains energy over time and flashes brightly for a moment when its energy is full.

import util

def test(filename, expected1, expected2):
    grid = util.load_grid(filename)
    print(filename, "loaded")

    result = solve1(grid.copy(), 100)
    print("Part 1.", result)
    util.assert_equal(result, expected1)

    result = solve2(grid.copy())
    print("Part 2.", result)
    util.assert_equal(result, expected2)

# Считаем количество вспышек за nstep поколений
def solve1(grid, nstep):
    return sum(step(grid) for _ in range(nstep))

# Найти поколение, когда будет вспышка во всех клетках
def solve2(matrix):
    nstep = 1
    while 100 != step(matrix):
        nstep += 1
    return nstep

def step(grid):
    '''
    You can model the energy levels and flashes of light in steps. During a single step, the following occurs:
    - First, the energy level of each octopus increases by 1.
    - Then, any octopus with an energy level >9 flashes. This increases the energy level of all adjacent octopuses by 1. 
      If this causes an octopus to have an energy level greater than 9, it also flashes. 
      This process continues as long as new octopuses keep having their energy level increased beyond 9. 
      (An octopus can only flash at most once per step.)
    - Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.
    '''
    for p in grid:
        grid[p] += 1

    sum = 0
    flashes = 1
    while (flashes):
        flashes = 0
        for p,v in grid.items():
            if v > 9:
                flash(grid, p)
                flashes += 1
                            
        sum += flashes

    return sum

# обнулить клетку и увеличить соседние, если они еще не обнулялись
def flash(grid, p):
    grid[p] = 0
    for d in util.NEAR8:
        p2 = p + d
        if p2 in grid and grid[p2] > 0: # not flashed yet
            grid[p2] += 1


test("input_sample.txt", 1656, 195)
test("input.txt", 1735, 400)