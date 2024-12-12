# AoC 2020. Day 11. Game of Life for seats.
import util


def test1(fname, expected):
    data = util.load_str_lines_list(fname)
    result = 0

    util.assert_equal(result, expected)


def parse(data):
    seats =[]
    for line in data:
        seats.append(list(line))
    return seats


def occupied(seats, i: int, j: int) -> int:
    result = 0
    pos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for p in pos:
        i2 = i; j2 = j
        while True:
            i2 += p[0]
            j2 += p[1]
            if i2 < 0 or i2 >= H or j2 < 0 or j2 >= W:
                break
            if seats[i2][j2] == 'L':
                break
            if seats[i2][j2] == '#':
                result += 1
                break

    return result


#    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
#    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
#    Otherwise, the seat's state does not change.
def apply_rules(seats):
    result = []
    for i in range(H):
        row = []
        for j in range(W):
            c = seats[i][j]
            c2 = c
            
            if c == '.':
                pass
            elif c == 'L':
                oc = occupied(seats, i, j)
                if not oc:
                    c2 = '#'
            elif c == '#':
                oc = occupied(seats, i, j)
                if oc >= 5:
                    c2 = 'L'
            
            row.append(c2)

        result.append(row)
    return result


def show(seats):
    for row in seats:
        print("".join(row))
    print()

data = util.load_str_lines_list('input.txt')
seats = parse(data)
H = len(seats)
W = len(seats[0])

while True:
#    show(seats)
    seats2 = apply_rules(seats)
    if seats == seats2:
        break
    seats = seats2

part2 = 0
for row in seats:
    for c in row:
        if c == '#':
            part2 += 1

print("Part 2.", part2)

# test1('input.txt', 0)

