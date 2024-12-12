# AoC 2020. Day 15: Rambunctious Recitation
# Memory game with elves:
# after the starting numbers, each turn results in that 
# player speaking aloud either 0 (if the last number is new) 
# or an age (if the last number is a repeat).
import util


def solve(input_list: str, max_turn: int) -> int:
    start_turn = len(input_list)
    last = input_list.pop()

    lastseen = {}
    for index, value in enumerate(input_list):
        lastseen[value] = index + 1 # +1 because turns start from 1

    for turn in range(start_turn, max_turn):
        if turn % 1000000 == 0: print(turn) # progress

        if last not in lastseen.keys():
            lastseen[last] = turn
            last = 0
        else:
            curr = turn - lastseen[last]
            lastseen[last] = turn
            last = curr
    
    return last

print("Part 1.")
util.assert_equal(solve([0,3,6], 2020), 436)
util.assert_equal(solve([5,2,8,16,18,0,1], 2020), 517)

print("Part 2.")
util.assert_equal(solve([0,3,6], 30000000), 175594)
util.assert_equal(solve([5,2,8,16,18,0,1], 30000000), 1047739)

