# Day 3: Rucksack Reorganization
# Поиск совпадающего элемента в 2х и 3х множествах.
import util

def test(filename, expected1, expected2):
    data = util.load_str_lines(filename)
    print(filename, "loaded")

    result = solve1(data)
    print("Part 1.", result)
    util.assert_equal(result, expected1)

    result = solve2(data)
    print("Part 2.", result)
    util.assert_equal(result, expected2)


def prio(a):
    if a.islower():
        return ord(a) - ord('a') + 1
    elif a.isupper():
        return ord(a) - ord('A') + 27
    raise RuntimeError(f"invalid char {a}")


def solve1(lines):
    result = 0
    for line in lines:
        middle = len(line) // 2
        comp1, comp2 = set(line[:middle]), set(line[middle:])
        a = comp1.intersection(comp2)
        if len(a) != 1:
            raise RuntimeError(f"invalid line {line}")
        common_ch = a.pop()
        priority = prio(common_ch)
        result += priority

    return result


def solve2(lines):
    result = 0
    for i in range(len(lines)//3):
        comp1, comp2, comp3 = set(lines[i*3]), set(lines[i*3+1]), set(lines[i*3+2])
        a = comp1.intersection(comp2).intersection(comp3)
        if len(a) != 1:
            raise RuntimeError(f"invalid line group {i*3}")
        common_ch = a.pop()
        priority = prio(common_ch)
        result += priority
    return result


test("input_sample.txt", 157, 70)
test("input.txt", 7850, 2581)
