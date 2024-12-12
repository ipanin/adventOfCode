import util
from collections import Counter

def test(filename, expected1, expected2):
    formula, rules = load(filename)
    print(filename, "loaded")

    result = solve1(formula, rules, 10)
    print("Part 1.", result)
    util.assert_equal(result, expected1)

    result = solve1(formula, rules, 40)
    print("Part 2.", result)
    util.assert_equal(result, expected1)


def solve1(formula, rules, nstep):
    for step in range(nstep):
        formula1 = formula[0]
        for i in range(len(formula)-1):
            s = formula[i:i+2]
            d = rules[s]
            formula1 += d + s[1]
        formula = formula1
        print(step)
    c = Counter(formula)
    return max(c.values()) - min(c.values())

def load(fname):
    with open(util.full_name(fname), 'rt') as f:
        formula, rules = f.read().rstrip().split('\n\n')

    rules1 = dict()
    for rule in rules.split('\n'):
        s, d = rule.split(" -> ")
        rules1[s] = d
    return formula, rules1


#test("input_sample.txt", 1588, 2188189693529)
test("input.txt", 2937, 0)