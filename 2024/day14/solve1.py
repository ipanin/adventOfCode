import time
from PIL import Image
import util

def solve1(lines: list[list[int]], W: int, H: int, seconds:int) -> int:
    robots = []
    for x, y, vx, vy in lines:
        robots.append((x + y * 1j, vx + vy * 1j))

    for _ in range(seconds):
        move(robots, W, H)
    return safety_factor(robots, W, H)

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

def show(lines: list[list[int]], W: int, H: int, time: int):
    robots = []
    for x, y, vx, vy in lines:
        robots.append((x + y * 1j, vx + vy * 1j))

    seconds = 0
    while seconds < time:
        seconds += 1
        move(robots, W, H)

    coords = [(r[0].real, r[0].imag) for r in robots]
    draw_image_bw(coords, W, H)

def draw_image_bw(coords: list, w: int, h: int):
    img = Image.new('L', (w, h), "black")
    pixels = img.load()  # Create the pixel map

    for c in coords:
        pixels[c] = 250

    img_r = img.resize((w*5, h*5), resample=Image.Resampling.BOX)
    img_r.show()

def move(robots, W: int, H: int):
    for i,r in enumerate(robots):
        pos = r[0] + r[1]
        r0 = complex(pos.real % W, pos.imag % H)
        robots[i] = (r0, r[1])

def safety_factor(robots, W: int, H: int):
    x1 = W // 2
    x2 = x1 + W % 2
    y1 = H // 2
    y2 = y1  + H % 2
    s = [0, 0, 0, 0]
    for robot in robots:
        pos = robot[0]
        if pos.real in range(0, x1):
            if pos.imag in range(0, y1):
                s[0] += 1
            elif pos.imag in range(y2, H):
                s[1] += 1
        elif pos.real in range(x2, W):
            if pos.imag in range(0, y1):
                s[2] += 1
            elif pos.imag in range(y2, H):
                s[3] += 1
    # multiply pos items
    return s[0] * s[1] * s[2] * s[3]

def density(robots, W: int, H: int):
    dx = W // 4
    dy = H // 4
    quadrants = {}

    for robot in robots:
        pos = robot[0]
        q = (pos.real // dx, pos.imag // dy)
        quadrants[q] = quadrants.get(q, 0) + 1

    return max(quadrants.values())



data = util.load_int_lists('sample.txt')
util.assert_equal(solve1(data, 11, 7, 100), 12, "Part 1, sample")


data = util.load_int_lists('input.txt')
util.assert_equal(solve1(data, 101, 103, 100), 225521010, "Part 1")

part2 = solve2(data, 101, 103)
util.assert_equal(part2, 0, "Part 2")
show(data, 101, 103, part2)
