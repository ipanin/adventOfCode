# Поиск маршрутов в лабиринте с возможностью срезать 1 препятствие
# найти кратчайший маршрут - главный
# вдоль маршрута пробовать убрать 1 препятсвие, если это не стена
# если выход на главном маршруте, то посчитать экономию
# иначе попробовать построить новый маршрут

import util

def solve1(matrix, min_economy: int) -> int:
    res = 0
    start = end = complex(0,0)
    walls = set()

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

    res = 0
    for pos in reversed(main_path):
        for n in util.NEAR4:
            cheet_pos = pos + n
            if cheet_pos not in walls:
                continue
            if cheet_pos + n not in visited:
                continue
            new_to_end = visited[cheet_pos+n]
            if visited[pos] - new_to_end - 2 >= min_economy:
                res += 1
    return res

matrix = util.load_char_matrix('sample.txt')
util.assert_equal(solve1(matrix, 37), 3, "Part 1 sample")

matrix = util.load_char_matrix('input.txt')
util.assert_equal(solve1(matrix, 100), 1375, "Part 1")
