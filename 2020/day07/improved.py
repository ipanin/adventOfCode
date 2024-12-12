# AoC 2020. Day 7: Handy Haversacks
import re
import util


def load_rules(fname: str):
    data = util.load_str_lines_list(fname)
    rules = dict()
    for line in data:
        outer, inner = parse_rule(line)
        rules[outer] = inner
    return rules


# Rule samples:
#   light red bags contain 1 bright white bag, 2 muted yellow bags.
#   vibrant chartreuse bags contain 1 mirrored white bag, 2 muted orange bags, 2 posh magenta bags.
def parse_rule(line: str):
    # (?'color'\w+ \w+) bags contain ((\d+) (\w+ \w+) bag[s,. ]+)+
    m = re.match(r'^(\w+ \w+) bags contain (.+)$', line)
    outer = m.group(1)
    all_inner = m.group(2)
    inners = dict()
    for i in re.findall(r'(\d+ \w+ \w+) bag[s,. ]+', all_inner):  # 2 muted orange:
        cnt, color = i.split(' ', 1)
        inners[color] = int(cnt)
    return outer, inners


# counter different colors
def countOuter(rules, color: str) -> int:
    def contains(super_col: str) -> bool:
        if super_col == color:
            return True
        return any(contains(inside_col) for inside_col in rules[super_col])

    return sum(contains(super_col) for super_col in rules) - 1


# count bag and all inner bags
def countInner(rules, color: str) -> int:
    return 1 + sum(cnt*countInner(rules, col) for col, cnt in rules[color].items())


# num of bag colors that contain 1+ 'shiny gold' bag
def test1(fname, expected):
    rules = load_rules(fname)
    result = countOuter(rules, 'shiny gold')
    util.assert_equal(result, expected)


def test2(fname, expected):
    rules = load_rules(fname)
    result = countInner(rules, 'shiny gold') - 1
    util.assert_equal(result, expected)


print("Part 1.")
test1('input0.txt', 4)
test1('input.txt', 208)

print("Part 2.")
test2('input0.txt', 32)
test2('input.txt', 1664)
