import util

def solve1(matrix) -> int:
    res = 0
    start = end = complex(0,0)
    direction = 1
    walls = set()
    paths = dict()

    for coord, c in matrix.items():
        if c == 'S':
            start = coord
        elif c == 'E':
            end = coord
        elif c == '#':
            walls.add(coord)

    while True:
        paths[start] = 0
        queue = [(start, direction)]
        while queue:
            coord, d = queue.pop(0)
            score = path_score(coord, d, paths, walls)
    return res

def path_score(pos, matrix) -> int:
    near = set([pos])
    for height in range(1,10):
        near_next = set()
        for n in near:
            near_next |= find_near(n, height, matrix)
        near = near_next

    return len(near)


matrix = util.load_char_matrix('sample1.txt')
util.assert_equal(solve1(matrix), 36, "Part1 sample")
#util.assert_equal(solve2(matrix), 81, "Part2 sample")

#matrix = util.load_digit_matrix('input.txt')
#util.assert_equal(solve1(matrix), 820, "Part1")
#util.assert_equal(solve2(matrix), 1786, "Part2")