import util

def solve1(start_list: list[int]) -> int:
    res = 0
    for seed in start_list:
        seq = generate1(seed, 2000)
        res += seq[-1]
    
    return res

def solve2(start_list: list[int]) -> int:
    seq_list = []
    for seed in start_list:
        seq = generate2(seed, 2000)
        seq_list.append(seq)

    patterns = find_good_patterns(seq_list)
    #patterns = [(-2,1,-1,3)]

    max_b = i = 0
    for pattern in patterns:
        i+=1
        if i%100 == 0:
            print('.', end='',flush=True)
        b = calc_price_total(seq_list, pattern)
        if b > max_b:
            max_b = b
            max_p = pattern
    print(max_p)
    return max_b

def generate1(seed, count) -> list[int]:
    seq = [seed]
    nxt = seed
    for _ in range(count):
        nxt = next(nxt)
        seq.append(nxt)
    return seq

def generate2(seed, count) -> tuple[list[int], list[int]]:
    seq = [seed]
    diff = [None]
    prev_price = seed%10
    rnd = seed
    for _ in range(count):
        rnd = next(rnd)
        price = rnd%10
        seq.append(price)
        diff.append(price-prev_price)
        prev_price = price
    
    return (seq,diff)

def find_good_patterns(seq_list):
    patterns = dict()
    for seq, diff in seq_list:
        for i in range(4, 2001):
            if seq[i] == 9:
                key = tuple(diff[i-3:i+1])
                if key in patterns:
                    patterns[key]+=1
                else:
                    patterns[key]=1
    sorted_keys = sorted(patterns, key=patterns.get, reverse=True)
    return sorted_keys[:1000]

def calc_price_total(seq_list, pattern) -> int:
    total = 0
    for seq,diff in seq_list:
        price = get_price(seq, diff, pattern)
        total += price
    return total

def get_price(seq, diff, pattern) -> int:
    for i in range(4,len(seq)):
        if tuple(diff[i-3:i+1]) == pattern:
            return seq[i]
    return 0

def next(n:int) -> int:
    n ^= n << 6
    n &= 0xffffff # % 2**24
    n ^= n >> 5
    n &= 0xffffff # % 2**24
    n ^= n << 11
    n &= 0xffffff # % 2**24
    return n
    


start_list = util.load_int_lines('sample1.txt')
util.assert_equal(solve1(start_list), 37327623, "Part 1 sample1")

start_list = util.load_int_lines('sample2.txt')
util.assert_equal(solve2(start_list), 23, "Part 2 sample2")

start_list = util.load_int_lines('input.txt')
util.assert_equal(solve1(start_list), 14691757043, "Part 1")
util.assert_equal(solve2(start_list), 1831, "Part 2")
