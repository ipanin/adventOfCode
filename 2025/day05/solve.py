# Дан список диапазонов вида
# a-b
# c-d
# После пустой строки дан набор идентификаторов.
# 1. Найти количество идентификаторов из диапазонов.
# 2. Найти суммарное количество всех идентификаторов внутри всех диапазонов
# (не учитывать повторы).

import util

def load(fname: str):
    fresh = []
    products = []
    with open(util.full_name(fname), 'rt', encoding='utf-8') as f:
        ranges = True
        for line in f.readlines():
            if ranges:
                if line == '\n':
                    ranges = False
                    continue
                start, end = line.split('-')
                fresh.append((int(start), int(end)))
            else:
                products.append(int(line))

    return fresh, products

def solve1(ranges, products) -> int:
    result = 0
    for p in products:
        for start, end in ranges:
            if start <= p <= end:
                result += 1
                break

    return result

def solve2(ranges) -> int:
    changed = True
    while changed:
        ranges, changed = optimize(ranges)

    result = 0
    for f in ranges:
        result += (f[1] - f[0] + 1)

    return result

def optimize(ranges):
    ranges_new = []
    changed = False
    for r in ranges:
        ranges_new, intersect = append_range(ranges_new, r)
        if intersect:
            changed = True

    return ranges_new, changed

def append_range(ranges, r):
    intersect = False
    result = []
    for r2 in ranges:
        if intersected(r, r2):
            result.append(union(r, r2))
            intersect = True
        else:
            result.append(r2)

    if not intersect:
        result.append(r)

    return result, intersect

def intersected(r1, r2):
    a1, b1 = r1
    a2, b2 = r2
    # касание считается пересечением
    return a1 in range(a2-1, b2+2) or b1 in range(a2-1, b2+2) or \
            a2 in range(a1-1, b1+2) or b2 in range(a1-1, b1+2)

def union(r1, r2):
    return (min(r1[0], r2[0]), max(r1[1], r2[1]))

fresh, products = load('sample.txt')
util.assert_equal(solve1(fresh, products), 3, "Part 1 Sample")
util.assert_equal(solve2(fresh), 14, "Part 2 Sample")

fresh, products = load('input.txt')
util.assert_equal(solve1(fresh, products), 615, "Part 1")
util.assert_equal(solve2(fresh), 353716783056994, "Part 2")
