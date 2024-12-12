import functools
import util

# Посчитать размножающиеся камни

def solve1(data, blinks_num) -> int:
    stones = data.split(' ')

    for _ in range(blinks_num):
        stones_new  = []
        for s in stones:
            if s == '0':
                stones_new.append('1')
            elif len(s) % 2 == 0:
                mid = len(s) // 2
                stones_new.append(s[:mid])
                stones_new.append(str(int(s[mid:])))
            else:
                stones_new.append(str(int(s) * 2024))

        stones = stones_new

    return len(stones)

def solve(data, blinks_num) -> int:
    stones = data.split(' ')
    res = 0
    for s in stones:
        print('.', end='')
        res += count_children(int(s), blinks_num)
    return res

@functools.cache
def count_children(stone: int, blinks_num: int) -> int:
    if blinks_num == 0:
        return 1

    if stone == 0:
        return count_children(1, blinks_num-1)

    l = len(str(stone))
    if l % 2 == 0:
        mid = l // 2
        s1 = int(str(stone)[:mid])
        s2 = int(str(stone)[mid:])
        return count_children(s1, blinks_num-1) + count_children(s2, blinks_num-1)

    return count_children(stone * 2024, blinks_num-1)

sample = "125 17"
util.assert_equal(solve(sample, 25), 55312, "Part1 sample")

data = "0 37551 469 63 1 791606 2065 9983586"
util.assert_equal(solve(data, 25), 204022, "Part1")
util.assert_equal(solve(data, 75), 241651071960597, "Part2")
