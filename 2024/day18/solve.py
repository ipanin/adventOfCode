import util

def load_obstacles(filename):
    obstacles = []
    lines = util.load_int_lists(filename)
    for line in lines:
        obstacles.append(line[0]+ 1j*line[1])

    return obstacles

def solve1(obstacles: list[complex], width: int, height: int) -> int:
    start = complex(0,0)
    end = complex(width-1, height-1)

    step = 0
    visited = set([start])
    edge = set([start])
    obstacles_set = set(obstacles)
    while len(edge) > 0:
        step += 1
        edge_next = set()
        for e in edge:
            for d in util.NEAR4:
                next_pos = e + d
                if next_pos == end:
                    return step
                if next_pos.real in range(width) and next_pos.imag in range(height) \
                    and next_pos not in obstacles_set and next_pos not in visited:
                    visited.add(next_pos)
                    edge_next.add(next_pos)
        edge = edge_next

    return -1

def solve2(obstacles: list[complex], width: int, height: int) -> complex:
    for i in range(1024, len(obstacles)):
        if i % 100 == 0: print(i)
        if solve1(obstacles[:i], width, height) == -1:
            return obstacles[i-1]
    return 0

obstacles = load_obstacles('sample1.txt')
util.assert_equal(solve1(obstacles[:12], 7, 7), 22, "Part 1 sample")

obstacles = load_obstacles('input.txt')
util.assert_equal(solve1(obstacles[:1024], 71, 71), 372, "Part 1")
util.assert_equal(solve2(obstacles, 71, 71), 25+6j, "Part 2")
