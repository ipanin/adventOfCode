# Aoc2021 Day 6: Lanternfish
# Part 1.
import util


# Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, 
# while each other number decreases by 1 if it was present at the start of the day.
def solve(data, days):
    arr  = data
    for day in range(days):
        print(f"Day {day+1}, len={len(arr)}")
        next = []
        for d in arr:
            if d == 0:
                next.append(6)
                next.append(8)
            else:
                next.append(d-1)
        arr = next
    return len(arr)

data = util.load_int_list('input.txt')
result = solve(data, 80)
print("Part 1.", result)
util.assert_equal(result, 385391)
