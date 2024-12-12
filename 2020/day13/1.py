# AoC 2020. Day
import collections
import math
import re
import os
import util


start = 1001796
ids = [37,41,457,13,17,23,29,431,19]
curr = start
while True:
    for id in ids:
        if curr % id == 0:
            print((curr-start)*id)
            exit(0)
    curr += 1
        

# print("Part 1.")

