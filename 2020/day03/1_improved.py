# AoC 2020. Day 3. Toboggan Trajectory
import util


def calc_trees(lines, dx: int, dy: int) -> int:
    heigth = len(lines)
    width = len(lines[0])
    x = y = count = 0

    while y < heigth:
        if lines[y][x % width] == '#':
            count += 1
        x += dx
        y += dy
    return count


def test2(lines, angles, expected):
    result = 1
    for a in angles:
        result *= calc_trees(lines, a[0], a[1])

    util.assert_equal(result, expected)


lines = util.load_str_lines_list('input.txt')

print("Part 1.")
result = calc_trees(lines, 3, 1)
util.assert_equal(result, 280)

print("Part 2.")
test2(lines, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)], 4355551200)
