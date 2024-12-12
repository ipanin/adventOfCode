# Day 8: Treetop Tree House
# Анализ матрицы высот

Directions = [(0,-1), (-1,0), (1,0), (0,1)]

def load_matrix(fname):
    grid = {}
    with open(fname, 'rt') as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.rstrip()):
                grid[(x,y)] = int(c)
    return grid, x+1, y+1

grid, sizeX, sizeY = load_matrix('input.txt')

# проверить, будет ли видно дерево (x,y) высоты h, если смотреть с направления (dx,dy)
def is_visible(h, x, y, dx, dy):
    while True:
        x += dx; y += dy
        if x not in range(sizeX) or y not in range(sizeY):
            return True
        if grid[(x, y)] >= h:
            return False

# посчитать количество деревьев в лесу, которые видны с любого из направлений
visible_trees = 0
for y in range(sizeY):
    for x in range(sizeX):
        h = grid[(x,y)]
        for dx,dy in Directions:
            if is_visible(h, x,y, dx,dy):
                visible_trees += 1
                break

print("Part1", visible_trees)  # 1776

###############################################################################

def scenic_score(x0, y0):
    h = grid[(x0,y0)]
    res = 1
    for dx, dy in Directions:
        res *= count_trees(h, x0, y0, dx, dy)
    return res

# посчитать количество деревьев, видных с дерева (x,y) высотой h в направлении (dx,dy)
def count_trees(h, x, y, dx, dy):
    count = 0
    while 0 < x < sizeX-1 and 0 < y < sizeY-1:
        x += dx; y += dy
        count += 1
        if grid[(x, y)] >= h:
            break
    return count


p2 = max(scenic_score(x,y) for y in range(sizeY) for x in range(sizeX))
print("Part2", p2)  # 234416