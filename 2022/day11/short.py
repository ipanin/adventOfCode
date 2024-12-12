import math
import re

BLOCK = 7
regex = re.compile(r"\d+")
def find_int(line):
    return int(regex.findall(line)[0])

def solve(content, rounds, part2=False):
    monkey_items       = [[int(x) for x in regex.findall(line)] for line in content[1::BLOCK]]
    monkey_operations  = [line.split(' = ')[1] for line in content[2::BLOCK]]
    monkey_test        = [find_int(line) for line in content[3::BLOCK]]
    monkey_conditions1 = [find_int(line) for line in content[4::BLOCK]]
    monkey_conditions2 = [find_int(line) for line in content[5::BLOCK]]

    n_monkeys = len(monkey_test)
    inspections = [0] * n_monkeys
    modulo = math.lcm(*monkey_test)

    for _ in range(rounds):
        for m in range(n_monkeys):
            items = monkey_items[m]
            for item in items:
                new = eval(monkey_operations[m], {"old": item})
                if part2 == 1:
                    new %= modulo
                else:
                    new //= 3
                new_monkey = monkey_conditions1[m] if new % monkey_test[m] == 0 else monkey_conditions2[m]
                monkey_items[new_monkey].append(new)
                inspections[m] += 1
            monkey_items[m] = []
    inspections.sort(reverse=True)
    return inspections[0] * inspections[1]

content = open("input.txt", "rt").read().splitlines()
print("Part 1:", solve(content, 20))
print("Part 2:", solve(content, 10000, part2=True))
