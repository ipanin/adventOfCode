import util
#import gutil

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
    return 0


def load(fname):
    with open(util.full_name(fname), 'rt') as f:
        coords, folds = f.read().rstrip().split('\n\n')

    return folds.split('\n')


#test("input_sample.txt", 0, 0)
test("input.txt", 0, 0)