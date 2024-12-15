import util
import gutil

def solve2(lines: list[list[int]], W: int, H: int) -> int:
    robots = []
    for x, y, vx, vy in lines:
        robots.append((x + y * 1j, vx + vy * 1j))

    seconds = 0
    max_density = 100
    res_seconds = 0
    while seconds < 10000:
        seconds += 1
        move(robots, W, H)
        f = density(robots, W, H)
        if f > max_density:
            max_density = f
            res_seconds = seconds

    return res_seconds

def move(robots, W: int, H: int):
    for i,r in enumerate(robots):
        pos = r[0] + r[1]
        r0 = complex(pos.real % W, pos.imag % H)
        robots[i] = (r0, r[1])

def density(robots, W: int, H: int):
    dx = W // 4
    dy = H // 4
    quadrants = {}

    for robot in robots:
        pos = robot[0]
        q = (pos.real // dx, pos.imag // dy)
        quadrants[q] = quadrants.get(q, 0) + 1

    return max(quadrants.values())

def show(lines: list[list[int]], W: int, H: int, time: int):
    robots = []
    for x, y, vx, vy in lines:
        robots.append((x + y * 1j, vx + vy * 1j))

    seconds = 0
    while seconds < time:
        seconds += 1
        move(robots, W, H)

    coords = [(r[0].real, r[0].imag) for r in robots]
    gutil.draw_image_bw(coords, W, H)


data = util.load_int_lists('input.txt')
part2 = solve2(data, 101, 103)
util.assert_equal(part2, 7774, "Part 2")
show(data, 101, 103, part2)
