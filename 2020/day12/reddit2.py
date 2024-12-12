import collections
import sys

lines = [l.rstrip('\n') for l in sys.stdin]

x, y = 0, 0
wx, wy = 10, 1

# part 1:
# dir = 0
# for line in lines:
#     action = line[:1]
#     arg = int(line[1:])
#     if action == 'F':
#         if dir % 360 == 0:
#             action = 'E'
#         if dir % 360 == 90:
#             action = 'N'
#         if dir % 360 == 180:
#             action = 'W'
#         if dir % 360 == 270:
#             action = 'S'
#     if action == 'N':
#         y += arg
#     if action == 'E':
#         x += arg
#     if action == 'S':
#         y -= arg
#     if action == 'W':
#         x -= arg
#     if action == 'L':
#         dir += arg
#     if action == 'R':
#         dir -= arg
#     assert action != 'F'

for line in lines:
    action = line[:1]
    value = int(line[1:])
    if action == 'F':
        x += wx * value
        y += wy * value
    if action == 'N':
        wy += value
    if action == 'E':
        wx += value
    if action == 'S':
        wy -= value
    if action == 'W':
        wx -= value
    if action == 'L':
        while value:
            wx, wy = -wy, wx
            value -= 90
    if action == 'R':
        while value:
            wx, wy = wy, -wx
            value -= 90

print(abs(x) + abs(y))

### https://github.com/daniel-dara/advent-of-code/blob/master/2020/day12/part2.py

cardinals = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
ship = 0, 0
waypoint = 10, 1

for line in open('input.txt'):
	action, value = line[0], int(line[1:])

	if action in cardinals:
		waypoint = waypoint[0] + value * cardinals[action][0], waypoint[1] + value * cardinals[action][1]
	elif action == 'F':
		ship = ship[0] + value * waypoint[0], ship[1] + value * waypoint[1]
	else:
		x, y = waypoint
		clockwise_degrees = {'L': 360 - value, 'R': value}[action]
		waypoint = {90: (y, -x), 180: (-x, -y), 270: (-y, x)}[clockwise_degrees]

print(sum(map(abs, ship)))