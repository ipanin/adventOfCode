# AoC 2020. Day 23: Crab Cups
# Circular cups game
#
# python -m cProfile -s cumulative 2.py
# C:\soft\pypy3.7-v7.3.3-win32\pypy3.exe 2.py
import itertools as it
from collections import deque
import util

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, data):
        node_prev = None
        self.index = dict()

        for d in reversed(data):
            node = Node(d)
            node.next = node_prev
            self.index[d] = node
            node_prev = node
        self.head = node
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def find(self, val):
        return self.index[val]
"""
L = 1000000
testlist = LinkedList(range(L))
for i in range(1000):
    testlist.find(L-i-1)
    print('.', end='')
"""

def move(cups, L: int):
    current = cups[0]
    pickup = []
    cups.rotate(-1)
    for i in range(3):
        pickup.append(cups.popleft())

    destination = current - 1
    if destination == 0:
        destination = L
    while destination in pickup:
        destination -= 1
        if destination == 0:
            destination = L

    dest_index = cups.index(destination)
    assert dest_index >= 0
    dest_index += 1 
    
    cups.rotate(-dest_index)
    cups.extend(pickup)
    cups.rotate(dest_index+3)
    #cups = cups[:dest_index] + pickup + cups[dest_index:]

def game(input: str, total, moves: int) -> int:
    cups = LinkedList(it.chain([int(x) for x in input], range(10, total+1))) # . total

    for m in range(moves):
        move(cups, total)
        if m+1 % 100000 == 0:
            print(m // 100000)
        #print(cups)
    
    start = cups.find(1).next
    return start.value * start.next.value

def solve(data):
    return 0



test1 = "389125467"
#util.assert_equal(game(test1, 1000000, 1000), 0)
#util.assert_equal(game(test1, 9, 10), 9*2)
#util.assert_equal(game(test1, 9, 100), 6*7)
#util.assert_equal(game(test1, 1000000, 10000000), 934001*159792)

#print("Part 1.")
#my_input = "253149867"
#util.assert_equal(game(my_input, 1000000, 10000000), 0)



