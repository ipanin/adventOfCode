import util

def solve1(lines: list[list[int]], width: int, height: int, seconds:int) -> int:
    robots = []
    for x, y, vx, vy in lines:
        robots.append((x + y * 1j, vx + vy * 1j))

    for _ in range(seconds):
        move(robots, width, height)

    return safety_factor(robots, width, height)

def move(robots, width: int, height: int):
    for i,r in enumerate(robots):
        pos = r[0] + r[1]
        r0 = complex(pos.real % width, pos.imag % height)
        robots[i] = (r0, r[1])

def safety_factor(robots, width: int, height: int) -> int:
    x1 = width // 2
    x2 = x1 + width % 2
    y1 = height // 2
    y2 = y1  + height % 2

    s = [0, 0, 0, 0]
    for robot in robots:
        pos = robot[0]
        if pos.real in range(0, x1):
            if pos.imag in range(0, y1):
                s[0] += 1
            elif pos.imag in range(y2, height):
                s[1] += 1
        elif pos.real in range(x2, width):
            if pos.imag in range(0, y1):
                s[2] += 1
            elif pos.imag in range(y2, height):
                s[3] += 1

    return s[0] * s[1] * s[2] * s[3]


data = util.load_int_lists('sample.txt')
util.assert_equal(solve1(data, 11, 7, 100), 12, "Part 1 (sample)")

data = util.load_int_lists('input.txt')
util.assert_equal(solve1(data, 101, 103, 100), 225521010, "Part 1")
