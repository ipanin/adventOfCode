import util
from functools import cache

@cache
def f(a):
    return f(a-9) + f(a-7) if a>0 else 1

def solve(arr, days):
    #return sum(f(days-t) for t in arr)
    res = 0
    for i,t in enumerate(arr):
        print(i)
        res += f(days-t)

data = util.load_int_list('input.txt')
result = solve(data, 80)
print("Part 1.", result)
util.assert_equal(result, 385391)

result = solve(data, 256)
print("Part 2.", result)
util.assert_equal(result, 1728611055389)

