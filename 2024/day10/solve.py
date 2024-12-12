import util

def solve1(matrix) -> int:
    res = 0
    for coord, height in matrix.items():
        if height == 0:
            res += trailhead_score(coord, matrix)
    return res

def trailhead_score(pos, matrix) -> int:
    near = set([pos])
    for height in range(1,10):
        near_next = set()
        for n in near:
            near_next |= find_near(n, height, matrix)
        near = near_next

    return len(near)

def find_near(pos, height, matrix) -> set[complex]:
    near = set()
    for n in util.NEAR4:
        npos = pos + n
        if npos in matrix and matrix[npos] == height:
            near.add(npos)
    return near

def solve2(matrix) -> int:
    res = 0
    for coord, height in matrix.items():
        if height == 0:
            res += trailhead_rating(coord, 1, matrix)
    return res

def trailhead_rating(pos, height, matrix) -> int:
    res = 0
    for n in util.NEAR4:
        npos = pos + n
        if npos in matrix and matrix[npos] == height:
            if height == 9:
                res += 1
            else:
                res += trailhead_rating(npos, height+1, matrix)

    return res

matrix = util.load_digit_matrix('input_sample.txt')
util.assert_equal(solve1(matrix), 36, "Part1 sample")
util.assert_equal(solve2(matrix), 81, "Part2 sample")

matrix = util.load_digit_matrix('input.txt')
util.assert_equal(solve1(matrix), 820, "Part1")
util.assert_equal(solve2(matrix), 1786, "Part2")