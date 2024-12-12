# not complete
import util

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
    summa = data[0]
    for d in data[1:]:
        summa = add(summa, d)
    return summa

def add(left, right):
    return reduce([left, right])

def reduce(n):
    while explode(n) or split(n):
        pass

    return n

def explode(n, level):
    a, b = n
    if type(a) is list:
        a1, left, right = explode(a, level+1)


    return n
    
def split(n):
    if type(n) is list:
        if not split(n[0]):
            split(n[1])
    elif n >= 10:
        return [n//2, n//2 + n%2]

def magnitude(n):
    if type(n) is list:
        return magnitude(n[0])*3 + magnitude(n[1])*2
    else:
        return n


def load(fname):
    lines = util.load_str_lines(fname)
    res = []
    for line in lines:
        res.append(eval(line))
    return res

#test("input_sample.txt", 0, 0)
test("input.txt", 0, 0)