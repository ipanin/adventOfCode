from functools import cache
import util

def load_data(filename):
    available = {}
    required = []
    with open(util.full_name(filename), 'rt', encoding='utf-8') as f:
        available_list = f.readline().rstrip().split(', ')
        for item in available_list:
            available[item] = len(item)
        for line in f.readlines():
            l = line.rstrip()
            if len(l):
                required.append(l)

    return available, required

def solve1(required: list[str]) -> int:
    count = 0
    for r in required:
        if possible(r):
            count += 1
    return count

@cache
def possible(r: str) -> bool:
    if len(r) == 1:
        return r in available
    if r in available:
        return True
    for index in range(1,len(r)):
        if possible(r[:index]) and possible(r[index:]):
            return True
    return False

def solve2_0(required: list[str]) -> int:
    count = 0
    for r in required:
        print('.', end='')
        solutions = all_possible1(r)
        count += len(solutions)
    return count

def solve2(required: list[str]) -> int:
    count = 0
    solution_dict = dict()
    for r in required:
        print('.', end='')
        solutions =all_possible(r, solution_dict)
        count += len(solutions)
    return count

@cache
def all_possible0(r: str) -> int:
    if len(r) == 1:
        return r in available
    count = 0
    if r in available:
        count += 1
    for index in range(1,len(r)):
        c1 = all_possible(r[:index])
        c2 = all_possible(r[index:])
        if c1 and c2:
            count += c1 * c2
    return count

@cache
def all_possible1(req: str) -> list:
    if len(req) == 1:
        if req in available:
            return [req]
        return []

    solutions = set()
    if req in available:
        solutions.add(req)
    for index in range(1,len(req)):
        solutions1 = all_possible(req[:index])
        solutions2 = all_possible(req[index:])
        for s1 in solutions1:
            for s2 in solutions2:
                solutions.add(s1 +  "," + s2)

    return sorted(solutions)

def all_possible(req: str, solution_dict: dict):
    if req in solution_dict:
        return solution_dict[req]

    solutions = set()
    if req in available:
        solutions.add(req)

    if len(req) == 1:
        return solutions

    for index in range(1,len(req)):
        solutions1 = all_possible(req[:index], solution_dict)
        if len(solutions1) == 0:
            continue
        solutions2 = all_possible(req[index:], solution_dict)
        if len(solutions2) == 0:
            continue
        for s1 in solutions1:
            for s2 in solutions2:
                solutions.add(s1 +  "," + s2)

    solution_dict[req] = solutions
    return solutions


available, required = load_data('sample.txt')
util.assert_equal(solve1(required), 6, "Part 1 sample")
possible.cache_clear()

#util.assert_equal(solve2(required), 16, "Part 2 sample")
#all_possible.cache_clear()

available, required = load_data('input.txt')
util.assert_equal(solve1(required), 283, "Part 1")
possible.cache_clear()

util.assert_equal(solve2(required), 0, "Part 2")
#all_possible.cache_clear()
