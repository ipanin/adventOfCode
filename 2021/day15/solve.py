# Day 15. Chiton
# Использую адаптированный метод Дейкстры поиска кратчайшего пути на графе. Вместо графа - матрица весов (рисков).
# Для вычисления второй части требуется использование pypy3
import util

INF = 1_000_000_000_000

def test(filename, expected1, expected2):
    weight = load(filename)
    print(filename, "loaded")

    result = solve(weight)
    print("Part 1.", result)
    util.assert_equal(result, expected1)

    result = solve(scaleMap(weight))
    print("Part 2.", result)
    util.assert_equal(result, expected2)

# Возвращает длину кратчайшего пути по матрице с весами клеток.
def solve(weight):
    sizeX = len(weight[0])
    sizeY = len(weight)

    totals = dict()
    totals[(0, 0)] = 0 # Длина пути до стартовой точки = 0

    optimized = True
    while optimized:
        optimized = False
        totals_new = totals.copy()
        for k,v in totals.items():
            x,y = k
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                if update_totals(totals_new, x+dx, y+dy, v, weight, sizeX, sizeY):
                    optimized = True
        totals = totals_new

    return totals[(sizeX-1, sizeY-1)] # длина пути до конечной точки

def update_totals(totals, x, y, v, weight, sizeX, sizeY):
    updated = False
    if 0 <= x < sizeX and 0 <= y < sizeY:
        current = totals.get((x,y), INF)
        new = v + weight[y][x]
        if new < current:
            totals[(x,y)] = new
            updated = True
    return updated

def load(fname):
    weight = []
    with open(util.full_name(fname), 'rt') as f:
        for line in f.readlines():
            x = line.rstrip()
            if len(x):
                weight.append([int(item) for item in x])

    return weight

def scaleMap(weight1):
    size1X = len(weight1[0])
    size1Y = len(weight1)

    sizeX = size1X*5
    sizeY = size1Y*5

    weight = []
    for y in range(sizeY):
        line = weight1[y % size1Y]*5
        for x in range(sizeX):
            line[x] = (weight1[y % size1Y][x % size1X] + y//size1Y + x//size1X - 1) % 9 + 1
        weight.append(line)
    return weight

test("input_sample.txt", 40, 315)
test("input.txt", 673, 2893)