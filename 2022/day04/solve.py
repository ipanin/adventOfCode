# Day 4: Camp Cleanup
# Определение вложенных и пересекающихся пар интервалов

import util

data = util.load_int_lists("input.txt")
part1 = part2 = 0
for a, b, c, d in data:
    X = range(a, b + 1)
    Y = range(c, d + 1)
    if a in Y and b in Y or c in X and d in X:
        part1 += 1
    if a in Y or b in Y or c in X or d in X:
        part2 += 1
print("Part 1.", part1)  # 595
print("Part 2.", part2)  # 952
