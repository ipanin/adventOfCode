# Day 12: Passage Pathing
# Поиск всех путей на графе, при условии, что некоторые вершины можно посещать только 1 раз

import util
from collections import defaultdict, Counter

def test(filename, expected1, expected2):
    adj = load_graph(filename)
    print(filename, "loaded")

    result = len(paths(adj, ['start']))
    print("Part 1.", result)
    util.assert_equal(result, expected1)

    result = len(paths2(adj, ['start']))
    print("Part 2.", result)
    util.assert_equal(result, expected2)

def load_graph(fname):
    lines = util.load_str_lines(fname)
    adj = defaultdict(set)
    for line in lines:
        a,b = line.split('-')
        adj[a].add(b)
        adj[b].add(a)
    
    return adj

def paths(adj, path):
    '''
    Вернуть список путей, при условии, что вершины в нижем регистре 
    можно посещать только 1 раз
    '''
    res = [] # list of lists
    verts = adj[path[-1]] # adjacent to last vertice
    
    for v in verts:
        if v == 'end':
            res.append(path + [v])
        elif v=='start': 
            continue
        elif v.islower() and v in path: # already visited
            continue
        else:
            res.extend(paths(adj, path + [v]))
    
    return res

def paths2(adj, path):
    '''
    Вернуть список путей, при условии, что 1 вершину в нижем регистре 
    можно посетить 2 раза, а остальные такие - только 1 раз
    '''
    res = [] # list of lists
    verts = adj[path[-1]] # adjacent to last vertice
    
    for v in verts:
        if v == 'end':
            res.append(path + [v])
            continue
        elif v=='start': 
            continue
        elif v.islower():
            c = Counter(p for p in path if p.islower())
            if max(c.values()) > 1 and v in path:
                continue # there is a vertice visited twice, and this vertice alredy visited
        res.extend(paths2(adj, path + [v]))
    
    return res

test("input_sample.txt", 10, 36)
test("input.txt", 4011, 108035)