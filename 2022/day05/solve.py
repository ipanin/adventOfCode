# --- Day 5: Supply Stacks ---
# Перестановка между стопками по инструкции
# В части 2 можно переставлять сразу несколько элементов.

import util
import re
from collections import deque

def test(filename, expected1, expected2):
    stack_text, commands = util.load_str_blocks("input.txt")
    print(filename, "loaded")

    result = solve1(stack_text, commands)
    print("Part 1.", result)
    util.assert_equal(result, expected1)

    result = solve2(stack_text, commands)
    print("Part 2.", result)
    util.assert_equal(result, expected2)


def solve1(stack_text, commands):
    stacks = init_stacks(stack_text)
    for line in commands:
        count, src, dest = map(int, re.findall('\d+', line))  # [int(x) for x in line.split()[1::2]]
        for _ in range(count):
            stacks[dest-1].append(stacks[src-1].pop())
    return get_top_elements(stacks)


def solve2(stack_text, commands):
    stacks = init_stacks(stack_text)
    for line in commands:
        count, src, dest = map(int, re.findall('\d+', line))
        buffer = []
        for _ in range(count):
            buffer.append((stacks[src-1].pop()))
        for i in range(count):
            stacks[dest-1].append(buffer[count-i-1])
    return get_top_elements(stacks)


def init_stacks(stack_text):
    n_stacks = (len(stack_text[0]) + 1) // 4
    stacks = [deque() for _ in range(n_stacks)]
    for line in reversed(stack_text[:-1]):
        for i, crate in enumerate(line[1::4]):
            if crate != ' ':
                stacks[i].append(crate)
    return stacks


def get_top_elements(stacks):
    res = []
    for s in stacks:
        res.append(s.pop())
    return "".join(res)


test("input.txt", "CVCWCRTVQ", "CNSCZWLVT")
