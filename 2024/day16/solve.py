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
    edge = set([(start, direction)])

    while len(edge) > 0:
        edge_next = set()
        for e in edge:
            score = visited[e]
            pos, dir = e

            next_dir = dir
            next_pos = pos + next_dir
            next_score = score + 1
            if next_pos not in walls:
                pair = (next_pos, next_dir)
                if pair in visited and visited[pair] > next_score or pair not in visited:
                    visited[pair] = next_score
                    edge_next.add((next_pos, next_dir))

            for d in util.NEAR4:
                if d == dir: continue
                next_dir = d
                next_pos = pos + next_dir
                next_score = score + 1001
                if next_pos not in walls:
                    pair = (next_pos, next_dir)
                    if pair in visited and visited[pair] > next_score or pair not in visited:
                        visited[pair] = next_score
                        edge_next.add((next_pos, next_dir))
        edge = edge_next
    return visited

# определить минимальную цену позиции среди всех 4х направлений
def min_score_of(pos: complex, visited):
    min_score = 2**32
    for d in util.NEAR4:
        if (pos, d) in visited and visited[(pos,d)] < min_score:
            min_score = visited[(pos,d)]
    return min_score

def solve2(matrix) -> int:
    walls, start, end = parse_labirint(matrix)
    visited = discover_labirint(walls, start)

    trail = { end }
    #edge = set([(end, direction)])
    curr = end
    #while curr != start:
        #for d in util.NEAR4:
            #next_pos = curr + d
            #if score_of(next_pos)

    return -1

matrix = util.load_char_matrix('sample1.txt')
util.assert_equal(solve1(matrix), 7036, "Part 1 sample 1")
util.assert_equal(solve2(matrix),   45, "Part 2 sample 1")

matrix = util.load_char_matrix('sample2.txt')
util.assert_equal(solve1(matrix), 11048, "Part 1 sample 2")
util.assert_equal(solve2(matrix),    64, "Part 2 sample 2")

matrix = util.load_char_matrix('input.txt')
util.assert_equal(solve1(matrix), 106512, "Part 1")
util.assert_equal(solve2(matrix), 0, "Part 2")
