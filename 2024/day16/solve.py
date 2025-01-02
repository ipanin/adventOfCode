# поиск кратчайшего пути в лабиринте.
# шаг стоит 1, поворот на 90 градусов стоит 1000.
# Начало с точки S, ориентация на восток.
# Часть 1. Найти цену самого короткого пути от S до E.
# Часть 2. Сколько плиток входят в любой кратчайший путь от S до E.
import util

def solve1(matrix) -> int:
    walls, start, end = parse_labirint(matrix)
    visited = discover_labirint(walls, start)
    return min_score_of(end, visited)

def parse_labirint(matrix):
    start = end = complex(0,0)
    walls = set()
    for coord, c in matrix.items():
        if c == 'S':
            start = coord
        elif c == 'E':
            end = coord
        elif c == '#':
            walls.add(coord)
    return walls, start, end

def discover_labirint(walls, start):
    direction = 1+0j
    visited = { (start, direction): 0 }
    wave = set([(start, direction)])

    while len(wave) > 0:
        wave_next = set()
        for e in wave:
            score = visited[e]
            pos, dir = e
            next_pos = pos + dir
            next_score = score + 1
            if next_pos not in walls:
                next_pair = (next_pos, dir)
                if next_pair in visited and visited[next_pair] > next_score or next_pair not in visited:
                    visited[next_pair] = next_score
                    wave_next.add(next_pair)

            for turn in [1j, -1j]: # turn left/right
                next_dir = dir * turn
                next_pos = pos + next_dir
                next_score = score + 1001
                if next_pos not in walls:
                    next_pair = (next_pos, next_dir)
                    if next_pair in visited and next_score < visited[next_pair] or next_pair not in visited:
                        visited[next_pair] = next_score
                        wave_next.add((next_pos, next_dir))
        wave = wave_next
    return visited

# определить минимальную цену позиции среди всех 4х направлений
def min_score_of(pos: complex, visited):
    min_score = 2**32
    for d in util.NEAR4:
        if (pos, d) in visited and visited[(pos,d)] < min_score:
            min_score = visited[(pos,d)]
    return min_score

# определить направления, дающие минимальную цену позиции
def min_score_dir(pos: complex, visited):
    min_score = min_score_of(pos, visited)
    dirs = []
    for d in util.NEAR4:
        if (pos, d) in visited and visited[(pos,d)] == min_score:
            dirs.append(d)
    return dirs

def solve2(matrix) -> int:
    walls, start, end = parse_labirint(matrix)
    visited = discover_labirint(walls, start)

    trails = { end }
    wave = set()
    # найти направления прихода в данную клетку с минимальной ценой
    dirs = min_score_dir(end, visited)
    for d in dirs:
        # добавить эти клетки в следующую волну и в клетки маршрутов
        wave.add((end, d))

    while len(wave) > 0:
        wave_next = set()
        for e in wave:
            score = visited[e]
            pos, dir = e
            prev_pos = pos-dir
            prev_pair = (prev_pos, dir)
            # если возможен приход с клетки с тем же направлением с ценой -1р
            if prev_pair in visited and visited[prev_pair] == score-1:
                trails.add(prev_pos)
                wave_next.add(prev_pair)
            for turn in [1j, -1j]: # turn left/right
                prev_dir = dir * turn
                prev_pair = (prev_pos, prev_dir)
                # если возможен приход с клетки с перпендикулярным направлением с ценой -1001р
                if prev_pair in visited and visited[prev_pair] == score-1001:
                    trails.add(prev_pos)
                    wave_next.add(prev_pair)
        
        wave = wave_next

    return len(trails)

matrix = util.load_char_matrix('sample1.txt')
util.assert_equal(solve1(matrix), 7036, "Part 1 sample 1")
util.assert_equal(solve2(matrix),   45, "Part 2 sample 1")

matrix = util.load_char_matrix('sample2.txt')
util.assert_equal(solve1(matrix), 11048, "Part 1 sample 2")
util.assert_equal(solve2(matrix),    64, "Part 2 sample 2")

matrix = util.load_char_matrix('input.txt')
util.assert_equal(solve1(matrix), 106512, "Part 1")
util.assert_equal(solve2(matrix),    563, "Part 2")
