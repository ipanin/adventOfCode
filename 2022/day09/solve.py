import util

Direction = {"L": -1, "D": -1j, "R": 1, "U": 1j}

def test(filename, expected1, expected2):
    lines = util.load_str_lines(filename)
    print(filename, "loaded")

    result = solve(2, lines)
    print("Part 1.", result)
    util.assert_equal(result, expected1)

    result = solve(10, lines)
    print("Part 2.", result)
    util.assert_equal(result, expected2)

def solve(knots, lines):
    rope = [0] * knots
    field = {0}

    for line in lines:
        d, n = line.split()
        d = Direction[d]
        n = int(n)
        for _ in range(n):
            move(rope, 0, d)
            field.add(rope[-1])
    return len(field)

def move(rope, i, d):
    rope[i] += d
    if i == len(rope)-1:  # last
        return

    dist = rope[i] - rope[i+1]
    if abs(dist.real) <= 1 and abs(dist.imag) <= 1:
        return
    dx = dist.real // 2 if abs(dist.real) == 2 else dist.real
    dy = dist.imag // 2 if abs(dist.imag) == 2 else dist.imag
    d2 = complex(dx, dy)
    move(rope, i+1, d2)

test("input_sample.txt", 13, 1)
test("input_sample2.txt", 88, 36)
test("input.txt", 5619, 2376)