# Дана карта склада, на которой символом '@' отмечены рулоны.
# 1. Посчитать количество рулонов, у которых менее 4 соседей.
# 2. Если меньше 4 соседей, то рулон можно убрать. Посчитать количество рулонов,
#    которые можно убрать.
# Как можно оптимизировать: хранить в матрице только позиции рулонов, не хранить пустые.
import util

def solve1(matrix: dict[complex, str]) -> int:
    result = 0
    for pos, val in matrix.items():
        if val != '@':
            continue
        neib = 0
        for n in util.NEAR8:
            if matrix.get(pos+n, '') == '@':
                neib += 1
        if neib < 4:
            result += 1
    return result

def solve2(matrix: dict[complex, str]) -> int:
    total_removed = 0
    while True:
        removed = step(matrix)
        if removed == 0:
            return total_removed
        total_removed += removed

def step(matrix: dict[complex, str]) -> int:
    removed = 0
    for pos, val in matrix.items():
        if val != '@':
            continue
        neib = 0
        for n in util.NEAR8:
            if matrix.get(pos+n, '') == '@':
                neib += 1
        if neib < 4:
            removed += 1
            matrix[pos] = 'x'
    return removed


sample = util.load_char_matrix('sample.txt')
data = util.load_char_matrix('input.txt')

util.assert_equal(solve1(sample), 13, "Part 1 Sample")
util.assert_equal(solve1(data), 1376, "Part 1")

util.assert_equal(solve2(sample), 43, "Part 2 Sample")
util.assert_equal(solve2(data), 8587, "Part 2")
