import util

def solve1(start_list: list[int], nth: int) -> int:
    return sum(calc_nth(i, nth) for i in start_list)

def solve2(start_list: list[int]) -> int:
    res = 0
    for seed in start_list:
        b = calc_price(seed, [-2,1,-1,3])
        res += b
    return res

def calc_price_total(start_list: list[int], pattern) -> int:
    res = 0
    for seed in start_list:
        b = calc_price(seed, pattern)
        res += b
    return res

def calc_nth(seed, nth) -> int:
    res = seed
    for _ in range(nth):
        res = next(res)
    return res

def calc_price(seed, pattern) -> int:
    nxt = seed
    prev = seed
    res = 0
    p = 0
    for i in range(2000):
        nxt = next(nxt)
        d = nxt%10
        change = d-prev
        if pattern[p] == change:
            p +=1
        else:
            p = 0
        if p == 4:
            return d
        prev = d
    return 0

"""
    *64. Then mix, prune.
    // 32. Then mix, prune.
    *2048. Then mix, prune.
"""
def next0(n:int) -> int:
    n ^= n*64
    n %= 16777216
    n ^= n // 32
    n %= 16777216 
    n ^= n * 2048
    n %= 16777216 
    return n

def next(n:int) -> int:
    n ^= n << 6
    n &= 0xffffff # % 2**24
    n ^= n >> 5
    n &= 0xffffff # % 2**24
    n ^= n << 11
    n &= 0xffffff # % 2**24
    return n

start_list = util.load_int_lines('sample1.txt')
util.assert_equal(solve1(start_list, 2000), 37327623, "Part 1 sample1")

start_list = util.load_int_lines('sample2.txt')
util.assert_equal(solve2(start_list), 23, "Part 2 sample2")

start_list = util.load_int_lines('input.txt')
util.assert_equal(solve1(start_list, 2000), 14691757043, "Part 1")

#

