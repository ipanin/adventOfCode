import util
from collections import Counter

def test(filename, expected1, expected2):
    formula, rules = load(filename)
    print(filename, "loaded")

    result = solve(formula, rules, 10)
    print("Part 1.", result)
    util.assert_equal(result, expected1)

    result = solve(formula, rules, 40)
    print("Part 2.", result)
    util.assert_equal(result, expected2)


def solve(formula, rules, nstep):
    last = formula[-1]

    pair_counter = Counter()
    for i in range(len(formula)-1):
        pair_counter[formula[i:i+2]] += 1

    for _ in range(nstep):
        pair_counter1 = Counter()
        for pair,c in pair_counter.items():
            p1, p2 = rules[pair]
            pair_counter1[p1] += c
            pair_counter1[p2] += c
        pair_counter = pair_counter1
        #print('.', end='')
    
    char_counter = Counter()
    for pair, c in pair_counter.items():
        char_counter[pair[0]] += c
    
    char_counter[last] += 1
    return max(char_counter.values()) - min(char_counter.values())


def load(fname):
    with open(util.full_name(fname), 'rt') as f:
        formula, rules = f.read().rstrip().split('\n\n')

    rules1 = dict()
    for rule in rules.split('\n'):
        s, d = rule.split(" -> ")
        s1 = s[0] + d
        s2 = d + s[1]
        rules1[s] = [s1,s2]
    return formula, rules1


test("input_sample.txt", 1588, 2188189693529)
test("input.txt", 2937, 3390034818249)