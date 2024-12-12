# Day 8: Treetop Tree House
# Анализ матрицы высот
# Использую комплексные числа для координат.
import util

grid, sizeX, sizeY = util.load_grid("input.txt")

# проверить, будет ли видно дерево (x,y) с любой стороны
def is_visible4(x,y):
    for dir in util.NEAR4:
        pos = complex(x, y)
        h = grid[pos]
        # проверить, будет ли видно дерево? если смотреть с направления dir
        while True:
            pos += dir
            if pos.real not in range(sizeX) or pos.imag not in range(sizeY):
                return True
            if grid[pos] >= h:
                break
    return False


def scenic_score(x, y):
    pos = complex(x, y)
    h = grid[pos]
    res = 1
    for delta in util.NEAR4:
        count = 0
        p = pos
        while 0 < p.real < sizeX-1 and 0 < p.imag < sizeY-1:
            p += delta
            count += 1
            if grid[p] >= h:
                break
        res *= count
    return res


p1 = sum(is_visible4(x, y) for y in range(sizeY) for x in range(sizeX))
p2 = max(scenic_score(x, y) for y in range(sizeY) for x in range(sizeX))
print("Part1", p1)  # 1776
print("Part2", p2)  # 234416