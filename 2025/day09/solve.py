# Даны координаты клеток на плоскости
import itertools as it
import util

def area(pair):
    a,b = pair
    return (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)


def solve1(data) -> int:
    pairs = sorted(it.combinations(data, 2), key=area)
    return area(pairs[-1])

def solve2(data) -> int:
    count = 0
    for i, p1 in enumerate(data):
        for j, p2 in enumerate(data[i+1:]):
            if p1[0] == p2[0] or p1[1] == p2[1]:
                count+=1
    return count

sample_data = util.load_int_lists('sample.txt')
util.assert_equal(solve1(sample_data), 50, "Part 1 Sample")
util.assert_equal(solve2(sample_data), 24, "Part 2 Sample")

data = util.load_int_lists('input.txt')
util.assert_equal(solve1(data), 4776100539, "Part 1")
util.assert_equal(solve2(data), 0, "Part 2")
