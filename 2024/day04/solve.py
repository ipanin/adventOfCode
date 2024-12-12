import util

def solve1(grid) -> int:
    count = 0
    for g in grid.items():
        if g[1] != 'X':
            continue
        for direction in util.NEAR8:
            if word_is(grid, g[0], direction, 'MAS'):
                count += 1
    return count


def word_is(grid, center, direction, word):
    for i, char in enumerate(word):
        pos = center + direction * (i+1)
        if pos not in grid.keys() or grid[pos] != char:
            return False
    return True

def solve2(grid) -> int:
    words = ['MS', 'SM']
    count = 0
    for g in grid.items():
        if g[1] != 'A':
            continue
        center = g[0]
        backslash = word(grid, center, [-1-1j, 1+1j])
        slash = word(grid, center, [-1+1j, 1-1j])
        if backslash in words and slash in words:
            count += 1
    return count

def word(grid, center, directions):
    result = ''
    for direction in directions:
        pos = center + direction
        if pos in grid.keys():
            result += grid[pos]
    return result


grid = util.load_char_matrix('input_sample.txt')
util.assert_equal(solve1(grid), 18, "Part1")
util.assert_equal(solve2(grid), 9, "Part2")

grid = util.load_char_matrix('input.txt')
util.assert_equal(solve1(grid), 2358, "Part1")
util.assert_equal(solve2(grid), 1737, "Part2")

