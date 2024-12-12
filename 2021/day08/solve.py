# Day 8: Seven Segment Search

import util
from collections import Counter

def solve1(data):
    count = Counter()
    for s in data:
        digits = s.split(' | ')[1].split()
        row = [len(d) for d in digits]
        c = Counter(row)
        count += c

    return count[2] + count[3]+ count[4]+ count[7]

def decode(samples, digits):
    table = fill_table(samples)
    num = 0
    for i,d in enumerate(reversed(digits)):
        k = "".join(sorted(d))
        index = table[k]
        # table.index(k)
        num += index * 10**i
    
    return num

def fill_table(samples):
    display = [None] * 10

    for s in samples:
        k = "".join(sorted(s))
        match len(s):
            case 2: display[1] = s
            case 3: display[7] = s
            case 4: display[4] = s
            case 7: display[8] = s

    for s in samples:
        if len(s) == 5:
            if s.issuperset(set(display[1])):
                display[3] = s
            elif len(s.difference(set(display[4]))) == 3:
                display[2] = s
            else:
                display[5] = s
    
    for s in samples:
        if len(s) == 6:
            if len(s.difference(display[3])) == 1:
                display[9] = s
            elif len(s.difference(display[5])) == 1:
                display[6] = s
            else:
                display[0] = s

    res = dict(("".join(sorted(s)),i) for i,s in enumerate(display))
    assert res.get("") == None
    return res

def solve2(data):
    sum = 0
    for s in data:
        left, right = s.split(' | ')
        samples = [set(s) for s in left.split()]
        digits = [set(s) for s in right.split()]
        sum += decode(samples, digits)
    return sum

def test(filename, expected1, expected2):
    data = util.load_str_lines(filename)
    result = solve1(data)
    print("Part 1.", result)
    util.assert_equal(result, expected1)

    result = solve2(data)
    print("Part 2.", result)
    util.assert_equal(result, expected2)

#test("input_sample.txt", 37, 168)
test("input.txt", 476, 0)