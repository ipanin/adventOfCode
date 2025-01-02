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
        if is_possible(r):
            count += 1
    return count

def solve2(required: list[str]) -> int:
    count = 0
    for r in required:
        count += count_all_possible(r)
    return count

@cache
def is_possible(req: str) -> bool:
    for a in available:
        if a == req:
            return True
        if req.startswith(a) and is_possible(req[len(a):]):
            return True

    return False

@cache
def count_all_possible(req: str) -> int:
    result = 0
    for a in available:
        if a == req:
            result += 1
        elif req.startswith(a):
            result += count_all_possible(req[len(a):])

    return result


available, required = load_data('sample.txt')
util.assert_equal(solve1(required), 6, "Part 1 sample")
is_possible.cache_clear()

util.assert_equal(solve2(required), 16, "Part 2 sample")
count_all_possible.cache_clear()

available, required = load_data('input.txt')
util.assert_equal(solve1(required), 283, "Part 1")
is_possible.cache_clear()

util.assert_equal(solve2(required), 615388132411142, "Part 2")
count_all_possible.cache_clear()
