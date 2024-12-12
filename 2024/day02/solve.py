import util

def solve1(reports) -> int:
    return sum([is_safe(report) for report in reports])

def solve2(reports) -> int:
    return sum([is_safe2(report) for report in reports])

def is_safe(report) -> bool:
    inc = (report[1] - report[0]) > 0

    for i in range(len(report) - 1):
        diff = report[i+1] - report[i]
        curr_inc = diff > 0
        if curr_inc != inc:
            return False
        if abs(diff) > 3 or diff == 0:
            return False

    return True

def is_safe2(report) -> bool:
    if is_safe(report):
        return True

    for i in range(len(report)):
        if is_safe(report.copy().pop(i)):
            return True

    return False

reports = util.load_int_spaced_lists('input.txt')
util.assert_equal(solve1(reports), 326, "Part1")
util.assert_equal(solve2(reports), 381, "Part2")

