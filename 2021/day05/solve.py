# AoC 2021. Day 5. Hydrothermal Venture
# My solution. Is not short, but simple/
import util

def draw_vec(field, vec, diag):
    x1,y1,x2,y2 = vec

    if x1 == x2:
        for y in util.my_range(y1, y2):
            f = field.get((x1,y), 0) 
            field[(x1,y)] = f+1
    elif y1 == y2:
        for x in util.my_range(x1, x2):
            f = field.get((x,y1), 0) 
            field[(x,y1)] = f+1
    elif diag:
        for x,y in zip(util.my_range(x1, x2), util.my_range(y1, y2)):
            f = field.get((x,y), 0) 
            field[(x,y)] = f+1

def solve(vectors, diag):
    field = dict()
    for vec in vectors:
        draw_vec(field, vec, diag)
    res = 0
    for pos, val in field.items():
        if val >= 2:
            res += 1
    
    return res


vectors = util.load_int_arrays('input.txt')
result = solve(vectors, False)
print("Part 1.", result)
util.assert_equal(result, 5197)

result = solve(vectors, True)
print("Part 2.", result)
util.assert_equal(result, 18605)
