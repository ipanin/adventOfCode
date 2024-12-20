import util

def solve1(lines) -> int:
    result = 0
    for i in range(0, len(lines), 3):
        line = lines[i]
        line2 = lines[i+1]
        line3 = lines[i+2]
        ax, ay = line[0], line[1]
        bx, by = line2[0], line2[1]
        tx, ty = line3[0], line3[1]
       
        tokens = calc_tokens(ax, ay, bx,by, tx, ty)
        result += tokens
    return result

def solve2(lines) -> int:
    result = 0
    for i in range(0, len(lines), 3):
        line = lines[i]
        line2 = lines[i+1]
        line3 = lines[i+2]
        ax, ay = line[0],line[1]
        bx, by = line2[0],line2[1]
        tx, ty = 10000000000000+line3[0],10000000000000+line3[1]
       
        tokens = calc_tokens(ax, ay, bx,by, tx, ty)
        result += tokens
    return result

def calc_tokens(ax, ay, bx,by, tx, ty):
    m = (ax*ty-ay*tx) / (ax*by-ay*bx)
    if m%1 != 0:
        return 0
    n = (tx - m*bx) / ax
    if n%1 != 0:
        return 0

    # 3 tokens to push the A button and 1 token to push the B button
    return int(3*n + m)

lines = util.load_int_lists('sample.txt')
util.assert_equal(solve1(lines), 480, "Part 1 (sample)")

lines = util.load_int_lists('input.txt')
util.assert_equal(solve1(lines), 36571, "Part 1")

lines = util.load_int_lists('input.txt')
util.assert_equal(solve2(lines), 85527711500010, "Part 2")
