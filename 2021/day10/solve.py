# Day 10
import util

PAIR = {'(':')', '[':']', '{':'}', '<':'>'}

def test(filename, expected1, expected2):
    data = util.load_str_lines(filename)
    print(filename, "loaded")

    result = solve1(data)
    print("Part 1.", result)
    util.assert_equal(result, expected1)

    result = solve2(data)
    print("Part 2.", result)
    util.assert_equal(result, expected2)

def solve1(data):
    POINTS = {')': 3,']': 57, '}': 1197, '>': 25137}
    sum = 0
    for line in data:
        ch = check(line)
        if ch != None:
            sum += POINTS[ch]
   
    return sum

def check(line):
    d = []
    for ch in line:
        if ch in PAIR.keys():
            d.append(ch)
        elif ch in PAIR.values():
            if len(d) == 0:
                return ch
            last = d.pop()
            if PAIR[last] != ch:
                return ch
    return None

def solve2(data):
    scores = []
    POINTS = {'(': 1,'[': 2, '{': 3, '<': 4}
    for line in data:
        score = 0
        complete = check2(line)
        if complete != None:
            for c in complete:
                score *= 5
                score += POINTS[c]
            scores.append(score)
    scores.sort()
    return scores[len(scores) // 2]

def check2(line):
    d = []
    for ch in line:
        if ch in PAIR.keys():
            d.append(ch)
        elif ch in PAIR.values():
            if len(d) == 0:
                return None
            last = d.pop()
            if PAIR[last] != ch:
                return None
    if len(d) == 0:
        return None
    return reversed(d)

test("input.txt", 268845, 4038824534)