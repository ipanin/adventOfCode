# Day 21: Keypad Conundrum (головоломка)
import util
from functools import cache

NUM_KEYPAD_GRAPH = { 
    7:[4,8],   8:[5,7,9],   9:[6,8],
    4:[1,5,7], 5:[2,4,6,8], 6:[3,5,9],
    1:[2,4],   2:[0,1,3,5], 3:[0xA,2,6],
    0xA:[0,3], 0:[2,0xA]
}

NUM_KEYPAD_DIR = { 
    (7,8): '>', (7,4): 'v', 
    (8,7): '<', (8,5): 'v', (8,9): '>', 
    (9,8): '<', (9,6): 'v',
    (4,7): '^', (4,5): '>', (4,1): 'v', 
    (5,4): '<', (5,8): '^', (5,6): '>', (5,2): 'v', 
    (6,9): '^', (6,5): '<', (6,3): 'v',
    (1,4): '^', (1,2): '>', 
    (2,1): '<', (2,5): '^', (2,3): '>', (2,0): 'v', 
    (3,6): '^', (3,2): '<', (3,0xA): 'v',
    (0,2): '^', (0,0xA): '>',
    (0xA,0):'<', (0xA,3): '^'
}

DIRECTIONAL_KEYPAD = {
    'A': { 'A':'',    '^':'<',  '>':'v',  'v':'<v', '<':'v<<' },
    '^': { 'A':'>',   '^':'',   '>':'v>', 'v':'v',  '<':'v<' },
    '>': { 'A':'^',   '^':'<^', '>':'',   'v':'<',  '<':'<<'},
    'v': { 'A':'^>',  '^':'^',  '>':'>',  'v':'',   '<':'<'},
    '<': { 'A':'>>^', '^':'>^', '>':'>>', 'v':'>',  '<':''}
}

def solve(codes:list[str], num_robots: int) -> int:
    res = 0
    for code in codes:
        l = min_len(code, num_robots)
        res += l * int(code[:-1]) # чтобы преобразовать code в число, надо отбросить последнюю букву A
    return res

def min_len(code: str, num_robots: int) -> str:
    seqs = all_paths(code)
    return min(count_children(seq, num_robots-1) for seq in seqs)

def all_paths(code: str) -> list[str]:
    pos = 0xA
    full_paths = ['']
    for c in code:
        i = int(c, 16)
        full_paths = combine(full_paths, paths(NUM_KEYPAD_GRAPH, pos, i), 'A')
        pos = i

    return full_paths

@cache
def count_children(data: str, robots_num: int) -> int:
    if robots_num == 0:
        return len(data)

    next = dirpad2dir(data)
    words = next.split('A')
    return sum(count_children(word+'A', robots_num-1) for word in words[:-1]) # после последнего A нет команды.

def combine(start_paths: list[str], finish_paths: list[str], end: str) -> list[str]:
    res = []
    for s in start_paths:
        for f in finish_paths:
            res.append(s+f+end)
    
    return res

def dirpad2dir(code: str) -> str:
    pos = 'A'
    res = ''
    for c in code:
        res += DIRECTIONAL_KEYPAD[pos][c] + 'A'
        pos = c

    return res

def paths(pad: dict[int, list[int]], start: int, end: int) -> list[str]:
    dist = 0
    visited = { start : 0 }
    wave = set([start])
    while len(wave) > 0:
        dist += 1
        wave_next = set()
        for w in wave:
            for next_pos in pad[w]:
                if next_pos not in visited:
                    visited[next_pos] = dist
                    wave_next.add(next_pos)
        wave = wave_next

    return ways(end, visited[end], pad, visited)

# найти все пути в клетку finish c длиной dist
def ways(finish: int, dist: int, graph, visited) -> list[str]:
    res = []
    # можно прийти из клетки neighbor, если ее расстояние от начала меньше на 1
    for neighbor in graph[finish]:
        if visited[neighbor] == dist-1: 
            if dist == 1: # рядом начало маршрута
                res.append(NUM_KEYPAD_DIR[(neighbor, finish)])
            else:
                # определить, откуда можно прийти в соседнюю точку
                prev_ways = ways(neighbor, dist-1, graph, visited)
                
                for prev_way in prev_ways:
                    way = prev_way + NUM_KEYPAD_DIR[(neighbor, finish)]
                    res.append(way)

    return res

codes = util.load_str_lines('sample.txt')
util.assert_equal(solve(codes, 3), 126384, "Part 1 sample")

codes = util.load_str_lines('input.txt')
util.assert_equal(solve(codes, 3), 203814, "Part 1")
util.assert_equal(solve(codes, 26), 248566068436630, "Part 2")
