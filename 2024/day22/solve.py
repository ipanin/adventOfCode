import util

def solve1(start_list: list[int], nth: int) -> int:
    return sum(calc(i, nth) for i in start_list)

def solve2(start_list: list[int], nth: int) -> int:
    for start in start_list:
        calc2(start, nth)

def calc(start, nth) -> int:
    #print('.', end='')
    res = start
    for _ in range(nth):
        res = next(res)
    return res

def calc2(start, nth) -> int:
    res = start
    prev = start
    seq =[]
    changes = []

    for _ in range(nth):
        res = next(res)
        n = res%10
        seq.append(n)
        changes.append(n-prev)
        prev = n

    return res

"""
    *64. Then mix, prune.
    // 32. Then mix, prune.
    *2048. Then mix, prune.
"""
def next(n:int) -> int:
    n ^= n*64
    n %= 16777216
    n ^= n // 32
    n %= 16777216 
    n ^= n * 2048
    n %= 16777216 
    return n


start_list = util.load_int_lines('input.txt')
util.assert_equal(solve1(start_list, 2000), 0, "Part 1")

