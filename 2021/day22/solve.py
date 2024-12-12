# not complete
import util
from collections import defaultdict

def test(filename, expected1, expected2):
    data = load(filename)
    print(filename, "loaded")

    result = solve1(data)
    print("Part 1.", result)
    util.assert_equal(result, expected1)

    #result = solve2(data)
    #print("Part 2.", result)
    #util.assert_equal(result, expected2)


def solve1(data):
    grid = defaultdict()
    s = 0
    for cmd,coords in data:
        s += 1
        if cmd == 'on':
            switch_on(grid, coords)
        elif cmd == 'off':
            switch_off(grid, coords)
        print(f"Step {s}/{len(data)}: Grid size={len(grid)}")
    return len(grid)

def switch_on(grid, coords):
    for x in range(coords[0], coords[1]+1):
        for y in range(coords[2], coords[3]+1):
            for z in range(coords[4], coords[5]+1):
                grid[(x,y,z)] = 1

def switch_off(grid, coords):
    for x in range(coords[0], coords[1]+1):
        for y in range(coords[2], coords[3]+1):
            for z in range(coords[4], coords[5]+1):
                if (x,y,z) in grid:
                    del grid[(x,y,z)]

def load(fname):
    lines = util.load_str_lines(fname)
    res = []
    for line in lines:
        cmd, coords = line.split(" ")
        coords = util.findall_ints(coords)
        res.append([cmd, coords])
    return res

#test("input_sample.txt", 0, 0)
#test("input1.txt", 0, 0)
test("input.txt", 0, 0)
'''
on x=4..48,y=-44..10,z=-45..4
on x=-41..3,y=-28..23,z=-4..44
on x=-11..36,y=-3..47,z=-6..41
on x=-38..14,y=-23..22,z=-33..18
on x=-37..13,y=-43..5,z=-20..26
on x=-44..4,y=-8..43,z=2..46
on x=-41..6,y=-39..5,z=-25..20
on x=-8..42,y=-19..26,z=-45..9
on x=-21..31,y=-23..31,z=-47..6
on x=-33..20,y=-49..0,z=-23..28
off x=29..47,y=26..44,z=21..36
on x=0..49,y=-43..9,z=-21..28
off x=34..48,y=36..45,z=-13..0
on x=-4..42,y=-4..42,z=-45..1
off x=5..23,y=18..33,z=12..28
on x=-9..37,y=-7..37,z=-38..14
off x=18..30,y=13..28,z=1..19
on x=-43..10,y=-27..25,z=-36..16
off x=20..30,y=-46..-37,z=13..23
on x=-46..4,y=-2..47,z=-20..32
'''