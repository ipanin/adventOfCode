import util
import re

def load_str_ignore_newline(fname: str) -> str:
    result = ''
    with open(util.full_name(fname), 'rt') as f:
        for line in f.readlines():
            result += line.rstrip()

    return result

def solve1(text: str) -> int:
    muls = re.findall(r"mul\((\d+),(\d+)\)", text)
    return sum(int(mul[0]) * int(mul[1]) for mul in muls)


def solve2(text: str) -> int:
    do = True
    sum = 0
    for match in re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", text):
        if match.group(0) == "do()":
            do = True
        elif match.group(0) == "don't()":
            do = False
        elif do:
            sum += int(match[1]) * int(match[2])

    return sum


program = load_str_ignore_newline('input.txt')
util.assert_equal(solve1(program), 182619815, "Part1")
util.assert_equal(solve2(program),  80747545, "Part2")

