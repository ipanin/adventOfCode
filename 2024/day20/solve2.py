# Поиск маршрутов в лабиринте с возможностью однократно срезать до 19 препятствий
# - найти кратчайший маршрут - главный
# - вдоль маршрута пробовать убрать 1 препятсвие, если это не стена
# - и если выход на главном маршруте, то посчитать экономию

import util

def solve2(matrix, min_economy: int) -> int:
    cheet_path_count = 0
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

    dist_to_end = 0
    visited = { end : 0 }
    edge = set([end])
    while len(edge) > 0:
        dist_to_end += 1
        edge_next = set()
        for e in edge:
            for d in util.NEAR4:
                next_pos = e + d
                if next_pos not in walls and next_pos not in visited:
                    visited[next_pos] = dist_to_end
                    edge_next.add(next_pos)
        edge = edge_next

    main_path = [end]
    curr = end
    while curr != start:
        for n in util.NEAR4:
            next_pos = curr + n
            if next_pos in visited and visited[next_pos] == visited[curr] + 1:
                curr = next_pos
                break
        main_path.append(curr)

    cheet_path_count = 0
    max_cheet_time = 20
    for pos in reversed(main_path):
        for dx in range(-max_cheet_time, max_cheet_time+1):
            for dy in range(-max_cheet_time, max_cheet_time+1):
                cheet_time = abs(dx) + abs(dy)
                if cheet_time <= max_cheet_time:
                    cheet_pos = pos + dx + 1j*dy
                    if cheet_pos not in visited:
                        continue
                    new_to_end = visited[cheet_pos]
                    economy = visited[pos] - new_to_end - cheet_time
                    if economy >= min_economy:
                        cheet_path_count += 1
    return cheet_path_count

matrix = util.load_char_matrix('sample.txt')
util.assert_equal(solve2(matrix, 74), 7, "Part 2 sample")

matrix = util.load_char_matrix('input.txt')
util.assert_equal(solve2(matrix, 100), 983054, "Part 2")

