import util

def solve1(connection_list: list[str]) -> int:
    graph = to_graph(connection_list)
    res = 0
    for n, neibors in graph.items():
        for n1 in neibors:
            for n2 in neibors:
                if n1 != n2 and n2 in graph[n1]:
                    if n.startswith('t') or n1.startswith('t') or n2.startswith('t'):
                        res += 1
    return res // (3*2)

def solve2(connection_list: list[str]) -> str:
    graph = to_graph(connection_list)
    max_n = 0
    max_set = set()
    for n, neibors in graph.items():
        curr_n = 0
        curr_set = set([n])
        for n1 in neibors:
            for n2 in neibors:
                if n1 != n2 and n2 in graph[n1]:
                    curr_n += 1
                    curr_set.add(n1)
                    curr_set.add(n2)
        if curr_n > max_n:
            max_n = curr_n
            max_set = curr_set
    return ','.join(sorted(list(max_set)))

def solve1_1(connection_list: list[str]) -> int:
    graph = to_graph(connection_list)
    res = 0
    for n, neibors in graph.items():
        if not n.startswith('t'):
            continue
        for n1 in neibors:
            if not n1.startswith('t'):
                continue
            for n2 in neibors:
                if n1 != n2 and n2 in graph[n1] and n2.startswith('t'):
                    res += 1
    return res // (3*2)

def solve2_1(connection_list: list[str]) -> str:
    graph = to_graph(connection_list)
    max_n = 0
    max_set = set()
    for n, neibors in graph.items():
        curr_n = 1
        curr_set = set([n])
        for n1 in neibors:
            curr_set.add(n1)
            for n2 in neibors:
                if n1 != n2 and n2 in graph[n1]:
                    curr_n += 1
                    curr_set.add(n2)

        if curr_n > max_n:
            max_n = curr_n
            max_set = curr_set
    return ','.join(sorted(list(max_set)))

def to_graph(connection_list: list[str]):
    graph = {}
    for line in connection_list:
        a, b = line.split('-')
        if a==b:
            continue

        if a in graph:
            graph[a].add(b)
        else:
            graph[a] = set([b])

        if b in graph:
            graph[b].add(a)
        else:
            graph[b] = set([a])

    return graph

connection_list = util.load_str_lines('sample.txt')
util.assert_equal(solve1(connection_list), 7, "Part 1 sample")
util.assert_equal(solve2(connection_list), 'co,de,ka,ta', "Part 2 sample")

connection_list = util.load_str_lines('input.txt')
util.assert_equal(solve1(connection_list), 1077, "Part 1")
util.assert_equal(solve2(connection_list), 'bc,bf,do,dw,dx,ll,ol,qd,sc,ua,xc,yu,zt', "Part 2")

