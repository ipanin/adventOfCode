# AoC 2020. Day 11
import util


def parse(data):
    seats =[]
    for line in data:
        seats.append(list(line))
    return seats

def occupied(seats, i, j):
    result = 0
    pos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for p in pos:
        i2 = i + p[0]
        j2 = j + p[1]
        if i2 >= 0 and i2 < H and j2 >= 0 and j2 < W and seats[i2][j2] == '#':
            result += 1

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
                if oc >= 4:
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


part1 = 0
for row in seats:
    for c in row:
        if c == '#':
            part1 += 1

print("Part 1.", part1)

# test1('input.txt', 0)

