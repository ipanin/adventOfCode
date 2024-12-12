# AoC 2020. Day
import collections
import math
import re
import os
import util


start = 0
ids_str = "37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,457,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,23,x,x,x,x,x,29,x,431,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19"
#ids_str = "7,13,x,x,59,x,31,19"
ids = ids_str.split(',')

res = []
curr = start
for id in ids:
    if id != 'x':
        n = int(id)
        res.append((n, curr))
    curr +=1

print(res)

start = 100000000000000
curr = start
while True:
    fail = False
    #for id, offs in res:
    #    if (curr+offs) % id != 0:
    #        fail = True
    #        break
    #if [(37, 0), (41, 27), (457, 37), (13, 50), (17, 51), (23, 60), (29, 66), (431, 68), (19, 87)]
    if not fail:
        print("Part2", curr)
        break
    curr += res[0][0]
    if curr % 1000000 == 0:
        print(curr)
        
    

# print("Part 1.")

