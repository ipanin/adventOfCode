# AoC 2020. Day 23: Crab Cups
# Circular cups game
import itertools as it
import util

def move(curr:int, cups:list):
    L = len(cups)
    M = max(cups)
    pickup = []
    extract_index = curr + 1
    for i in range(3):
        if extract_index >= len(cups):
            extract_index = 0
        pickup.append(cups.pop(extract_index))
        if extract_index < curr:
            curr -= 1

    destination = cups[curr] - 1
    if destination == 0:
        destination = M
    while destination in pickup:
        destination -= 1
        if destination == 0:
            destination = M

    dest_index = cups.index(destination)
    assert dest_index >= 0
    dest_index += 1 
    
    cups = cups[:dest_index] + pickup + cups[dest_index:]
    if dest_index <= curr:
        curr += 3
    curr = (curr + 1) % L
    return curr, cups

def game(input: str, moves: int) -> str:
    cups = [int(x) for x in input]

    curr = 0
    for m in range(moves):
        curr, cups = move(curr, cups)
        #print(cups)
    
    start = cups.index(1)
    res = "".join(map(str, cups[start+1:] + cups[:start]))
    return res

def solve(data):
    return 0



test1 = "389125467"
util.assert_equal(game(test1, 10), "92658374")
util.assert_equal(game(test1, 100), "67384529")

print("Part 1.")
my_input = "253149867"
util.assert_equal(game(my_input, 100), "34952786")



