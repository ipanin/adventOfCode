# AoC 2020. Day 12 : Move by vector
import util

def move(x, y, direction, distance):
    if direction == 0:
        x += distance
    if direction == 1:
        y += distance
    if direction == 2:
        x -= distance
    if direction == 3:
        y -= distance
    return x, y

data0 = "F10 N3 F7 R90 F11".split() # example
data = util.load_str_lines_list('input.txt')
COMPASS = {'E':0, 'N':1, 'W':2, 'S':3}
DIRECTIONS = {'R90':3, 'R180':2, 'R270':1, 'L90':1, 'L180':2, 'L270': 3}

x = y = 0
direction = 0
for command in data:
    if command in DIRECTIONS:
        direction = (direction + DIRECTIONS[command]) % 4
    else:
        action = command[0]
        if action != 'F':
            direction_curr = COMPASS[action]
        else:
            direction_curr = direction

        value = int(command[1:])
        x, y = move(x,y, direction_curr, value)

print("Part 1. ", abs(x) + abs(y))  # 439

