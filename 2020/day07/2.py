# AoC 2020. Day
import re
import util


# light red bags contain 1 bright white bag, 2 muted yellow bags.
# vibrant chartreuse bags contain 1 mirrored white bag, 2 muted orange bags, 2 posh magenta bags.
def parse1(line: str):
    # (?'color'\w+ \w+) bags contain ((\d+) (\w+ \w+) bag[s,. ]+)+
    m = re.match(r'^(\w+ \w+) bags contain (.+)$', line)
    outer = m.group(1)
    inner = m.group(2)
    inner = re.findall(r'\d+ (\w+ \w+) bag[s,. ]+', inner)
    return outer, inner


def parse2(line: str):
    # (?'color'\w+ \w+) bags contain ((\d+) (\w+ \w+) bag[s,. ]+)+
    m = re.match(r'^(\w+ \w+) bags contain (.+)$', line)
    outer = m.group(1)
    inner = m.group(2)
    inner = re.findall(r'(\d+ \w+ \w+) bag[s,. ]+', inner)
    return outer, inner


def Outers(rules, color: str):
    result = []
    for outer, inners in rules.items():
        if color in inners:
            result.append(outer)
    return set(result)


def allOuters(rules, color: str):
    outers = Outers(rules, color)
    result = outers.copy()

    for o in outers:
        outers2 = allOuters(rules, o)
        result |= outers2

    return result


def countInner(rules, color: str) -> int:
    result = 1
    inners = rules[color]
    for i in inners:
        cnt, col = i.split(' ', 1)
        result += int(cnt) * countInner(rules, col)
    return result


def test1(fname, expected):
    data = util.load_str_lines_list(fname)
    rules = dict()
    for line in data:
        outer, inner = parse1(line)
        rules[outer] = inner

    result = len(allOuters(rules, 'shiny gold'))
    util.assert_equal(result, expected)


def test2(fname, expected):
    data = util.load_str_lines_list(fname)
    rules = dict()
    for line in data:
        outer, inner = parse2(line)
        rules[outer] = inner

    result = countInner(rules, 'shiny gold') - 1
    util.assert_equal(result, expected)


print("Part 1.")
test1('input0.txt', 4)
test1('input.txt', 208)

print("Part 2.")
test2('input0.txt', 32)
test2('input.txt', 1664)
