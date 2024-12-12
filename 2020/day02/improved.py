# AoC 2020. Day 2. Password Philosophy
import util
import re


# line = "8-12 z: zxzzzzfxzlmzz"
def valid1(line: str) -> bool:
    diap, letter, passw = line.split(' ')
    lo, hi = diap.split("-")
    letter = letter[0]

    cnt = passw.count(letter)
    return int(lo) <= cnt <= int(hi)


def valid2(line: str) -> bool:
    diap, letter, passw = line.split(' ')
    lo, hi = diap.split("-")
    letter = letter[0]

    a = passw[int(lo)-1]
    b = passw[int(hi)-1]

    # return (a == letter or b == letter) and (a != b)
    return (a == letter) != (b == letter)  # xor


def reddit_solution():
    lines = [re.split('[: -]', l.strip()) for l in open(r'C:\git\github\adventOfCode2020\day02\input.txt')]
    lines1 = [(int(p1), int(p2), pwd.count(ch)) for p1, p2, ch, _, pwd in lines]
    lines2 = [(pwd[int(p1)-1] == ch, pwd[int(p2)-1] == ch) for p1, p2, ch, _, pwd in lines]
    part1 = sum(n1 <= matches <= n2 for n1, n2, matches in lines1)
    part2 = sum(p1 ^ p2 for p1, p2 in lines2)
    print(part1, part2)


lines = util.load_str_lines_list('input.txt')

print("Part 1.")
result = sum(map(valid1, lines))
util.assert_equal(result, 548)

print("Part 2.")
result = sum(map(valid2, lines))
util.assert_equal(result, 502)

reddit_solution()
