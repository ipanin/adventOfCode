# Инструкция по открытию сейфа.
# 1. Посчитать количество нулей
# 2. Посчитать количество прохождений через нуль

import util

def solve1(start: int, instructions: list[str]) -> int:
    result = 0
    current = start
    for ins in instructions:
        d = int(ins[1:])
        if ins[0] == 'R':
            current += d
        else:
            current -= d

        current %= 100

        if current == 0:
            result += 1

    return result

def solve2(start: int, instructions: list[str]) -> int:
    result = 0
    current = start
    for ins in instructions:
        d = int(ins[1:])

        result += d // 100
        d %= 100

        if ins[0] == 'R':
            current += d
            if current >= 100:
                result += 1
        else:
            if d >= current and current != 0:
                result += 1
            current -= d

        current %= 100

    return result


instructions_sample = util.load_str_lines('input_sample.txt')
instructions = util.load_str_lines('input.txt')

util.assert_equal(solve1(50, instructions_sample), 3, "Part 1 Sample")
util.assert_equal(solve1(50, instructions), 980, "Part 1")

util.assert_equal(solve2(50, instructions_sample), 6, "Part 2 Sample")
util.assert_equal(solve2(50, instructions), 5961, "Part 2")
