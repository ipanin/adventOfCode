# not complete
import util
#from copy import deepcopy

def test(filename, expected1, expected2):
    data = load(filename)
    print(filename, "loaded")

    result = solve1(data)
    print("Part 1.", result)
    util.assert_equal(result, expected1)

    #result = solve2(data)
    #print("Part 2.", result)
    #util.assert_equal(result, expected2)

# find num of beacons
def solve1(data):
    others = range(1,len(data))
    for s1 in data:
        for i2 in others.copy():
            s2 = data[i2]
            dif = compare(s1, s2)

    return 0


def compare(s1, s2):
    for dir in range(24):
    s2r = rotate(s2, dir)
    for b1 in s1:
        for b2 in s2r:
            dif = sub_vec(b1,b2)
            s2d = add_vec(b2,dif)
            if intersect(s1, s2d) > 12:
                return

    return None

    
def load(fname):
    scanners = util.load_str_blocks(fname)
    data = []
    for s in scanners:
        d = []
        for line in s[1:]:
            d.append([int(item) for item in line.split(',')])
        data.append[d]
    return data

#test("input_sample.txt", 0, 0)
test("input.txt", 0, 0)