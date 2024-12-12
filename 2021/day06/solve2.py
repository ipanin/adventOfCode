# Aoc2021 Day 6: Lanternfish
# Part 1 and 2.
import util
from collections import Counter 

# Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, 
# while each other number decreases by 1 if it was present at the start of the day.
# Using Counter instead of list to optimize performance
def solve(data, days):
    arr  = Counter(data)
    # set all values to bypass RuntimeError: dictionary changed size during iteration
    for i in range(8+1):
        arr[i] = arr[i]

    for day in range(days):
        #print(f"Day {day+1}, len={sum(arr.values())}")
        zeros = arr[0]
        for i,d in enumerate(arr):
            arr[i] = arr[i+1]

        arr[6] += zeros
        arr[8] = zeros
    return sum(arr.values())

data = util.load_int_list('input.txt')

result = solve(data, 80)
print("Part 1.", result)
util.assert_equal(result, 385391)

result = solve(data, 256)
print("Part 2.", result)
util.assert_equal(result, 1728611055389)
