# Day 7: The Treachery of Whales
# Мое неоптимальное решение перебором. Но работает достаточно быстро
import util
1
def solve1(data):
    min_fuel = 1000000000
    best_target = -1
    for target in range(max(data)+1):
        fuel = sum([abs(target-x) for x in data])
        if fuel < min_fuel:
            min_fuel = fuel
            best_target = target
        #print(f"Target {target}, fuel={fuel}, min_fuel={min_fuel}")
    print(f"Best target {best_target}")
    return min_fuel

def progress(n):
    return int((n+1)*n/2)

def solve2(data):
    min_fuel = 1000000000
    for target in range(max(data)+1):
        fuel = sum([progress(abs(target-x)) for x in data])
        if fuel < min_fuel:
            min_fuel = fuel
        #print(f"Target {target}, fuel={fuel}, min_fuel={min_fuel}")
    return min_fuel


def test(filename, expected1, expected2):
    data = util.load_int_list(filename)

    result = solve1(data)
    print("Part 1.", result)
    util.assert_equal(result, expected1)

    result = solve2(data)
    print("Part 2.", result)
    util.assert_equal(result, expected2)

test("input_sample.txt", 37, 168)
test("input.txt", 343605, 96744904)