# AoC 2020. Day 12: Move by vector
import util


def rotate(pos, waypoint, rotation : int):
    dx = waypoint[0]-pos[0]
    dy = waypoint[1]-pos[1]
    if rotation == 1:
        dx, dy = -dy, dx
    if rotation == 2:
        dx, dy = -dx, -dy
    if rotation == 3:
        dx, dy = dy, -dx
    return [ pos[0]+dx, pos[1]+dy ]

def move_waypoint(pos, direction: int, distance: int):
    if direction == 0:
        pos[0] += distance
    if direction == 1:
        pos[1] += distance
    if direction == 2:
        pos[0]-= distance
    if direction == 3:
        pos[1] -= distance

def forward(pos, waypoint, steps: int):
    dx = waypoint[0]-pos[0]
    dy = waypoint[1]-pos[1]
    pos[0] += dx*steps
    pos[1] += dy*steps

    waypoint[0] += dx*steps
    waypoint[1] += dy*steps

data0 = "F10 N3 F7 R90 F11".split() # example
data = util.load_str_lines_list('input.txt')
COMPASS = {'E':0, 'N':1, 'W':2, 'S':3}
ROTATIONS = {'R90':3, 'R180':2, 'R270':1, 'L90':1, 'L180':2, 'L270': 3}

pos = [0,0]
waypoint = [10, 1]

for command in data:
    if command in ROTATIONS:
        rotation = ROTATIONS[command]
        waypoint = rotate(pos, waypoint, rotation)
    else:
        action = command[0]
        value = int(command[1:])
        if action == 'F':
            forward(pos, waypoint, value)
        else:
            move_waypoint(waypoint, COMPASS[action], value)

print("Part 2. ", abs(pos[0]) + abs(pos[1]))  # 12385


