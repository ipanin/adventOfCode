# AoC 2020. Day 11: Seating System.
# Game of Life for seats.
import util
import time


def parse(data):
    seats = []
    for line in data:
        seats.append(list(line))
    return seats

POS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
def occupied_near(seats, i, j):
    H, W = len(seats), len(seats[0])
    occupied = 0
    for p in POS:
        i2 = i + p[0]
        j2 = j + p[1]
        if 0 <= i2 < H and 0 <= j2 < W and seats[i2][j2] == '#':
            occupied += 1

    return occupied

def occupied_visible(seats, i: int, j: int) -> int:
    H, W = len(seats), len(seats[0])
    occupied = 0
    for p in POS:
        i2,j2 = i,j
        while True:
            i2 += p[0]
            j2 += p[1]
            if not (0 <= i2 < H and 0 <= j2 < W):
                break
            s = seats[i2][j2]
            if  s == 'L':
                break
            if s == '#':
                occupied += 1
                break
    return occupied


# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.
def new_state1(seats, i, j):
    c = seats[i][j]
    
    if c == '.':
        return c

    oc = occupied_near(seats, i, j)
    if c == 'L' and not oc:
        return '#'
    if c == '#' and oc >= 4:
        return 'L'

    return c


# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.
def new_state2(seats, i, j):
    c = seats[i][j]

    if c == '.': # no seat
        return c

    oc = occupied_visible(seats, i, j)
    if c == 'L' and not oc:
        return '#'
    if c == '#' and oc >= 5:
        return 'L'

    return c


def apply_rules(seats, new_state):
    H, W = len(seats), len(seats[0])
    result = []
    for i in range(H):
        row = []
        for j in range(W):
            row.append(new_state(seats, i, j))
        result.append(''.join(row))
    return result


def show(seats):
    for row in seats:
        print(row)
    print()


def test(fname: str, new_state, expected: int):
    data = util.load_str_lines_list(fname)
    seats = data
    while True:
    #    show(seats)
        seats2 = apply_rules(seats, new_state)
        if seats == seats2:
            break
        seats = seats2

    result = ''.join(seats).count('#')
    util.assert_equal(result, expected)

print("Part 1.")
test('input0.txt', new_state1, 37)

start = time.process_time()
test('input.txt', new_state1, 2346)
print("Elapsed", time.process_time() - start)

print("Part 2.")
test('input0.txt', new_state2, 26)

start = time.process_time()
test('input.txt', new_state2, 2111)
print("Elapsed", time.process_time() - start)
