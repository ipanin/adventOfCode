# Day 11: Monkey in the Middle
# Обезьянки перекидывают друг-другу предметы по правилам делимости
# Во второй части чтобы не проверять делимость больших чисел,
# после каждого вычисления большие числа делятся по модулю
import util
from math import lcm
from operator import attrgetter
from types import SimpleNamespace

# Monkey 0:
#   Starting items: 57, 58
#   Operation: new = old * 19
#   Test: divisible by 7
#     If true: throw to monkey 2
#     If false: throw to monkey 3
def load_data(fname):
    data = []
    blocks = util.load_str_blocks(fname)
    for lines in blocks:
        m = dict()
        m['items'] = util.findall_ints(lines[1])
        m['oper'] = lines[2].split('= ')[1]
        m['div'] = util.find_int(lines[3])
        m['m1'] = util.find_int(lines[4])
        m['m2'] = util.find_int(lines[5])
        data.append(SimpleNamespace(**m))
    return data

def solve(monkeys, rounds, part2=False):
    inspections = [0] * len(monkeys)
    modulo = lcm(*map(attrgetter('div'), monkeys))

    for _ in range(rounds):
        for i,m in enumerate(monkeys):
            for item in m.items:
                inspections[i] += 1
                new = eval(m.oper, {"old": item})
                if part2:
                    new %= modulo
                else:
                    new //= 3
                index = m.m1 if new % m.div == 0 else m.m2
                monkeys[index].items.append(new)
            m.items = []
    inspections.sort(reverse=True)
    return inspections[0] * inspections[1]

def test(fname):
    monkeys = load_data(fname)
    p1 = solve(monkeys, 20)
    util.assert_equal(p1, 50830, "Part1")

    monkeys = load_data(fname)
    p2 = solve(monkeys, 10000, part2=True)
    util.assert_equal(p2, 14399640002, "Part2")

test("input.txt")
