import util

def solve2(lines: list[str], direction_lines: list[str]) -> int:
    obstacles = set()
    boxes = dict()
    robot = 1j
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            pos = x*2 + y * 1j
            if c == '#':
                obstacles.add(pos)
                obstacles.add(pos+1)
            elif c == 'O':
                boxes[pos]='['
                boxes[pos+1]=']'
            elif c == '@':
                robot = pos

    for line in direction_lines:
        for d in line.rstrip():
            direction = util.DIRECTION_MAP[d]
            robot = move_robot(robot, direction, boxes, obstacles)

    return factor(boxes)

def move_robot(robot: complex, direction: complex, boxes: dict, obstacles: set) -> complex:
    next_pos = robot + direction

    if next_pos in obstacles:
        return robot
    elif next_pos not in boxes:
        return next_pos
    elif can_move_box(next_pos, direction, boxes, obstacles):
        move_box(next_pos, direction, boxes, obstacles)
        return next_pos
    else:
        return robot

def can_move_box(box_pos: complex, direction: complex, boxes: dict, obstacles: set) -> bool:
    if direction.real == 0:
        return can_move_box_v(box_pos, direction, boxes, obstacles)
    else:
        return can_move_box_h(box_pos, direction, boxes, obstacles)

def can_move_box_h(box_pos: complex, direction: complex, boxes: dict, obstacles: set) -> bool:
    next_pos = box_pos + direction

    if next_pos in obstacles:
        return False
    elif next_pos not in boxes:
        return True

    return can_move_box_h(next_pos, direction, boxes, obstacles)

def can_move_box_v(box_pos: complex, direction: complex, boxes: dict, obstacles: set) -> bool:
    b = boxes[box_pos]
    box_pos2 = box_pos + 1 if b == '[' else box_pos - 1

    next_pos = box_pos + direction
    next_pos2 = box_pos2 + direction

    if next_pos in obstacles or next_pos2 in obstacles:
        return False

    if next_pos in boxes and not can_move_box_v(next_pos, direction, boxes, obstacles):
        return False

    if next_pos2 in boxes and not can_move_box_v(next_pos2, direction, boxes, obstacles):
        return False

    return True

def move_box(box_pos: complex, direction: complex, boxes: dict, obstacles: set):
    if direction.real == 0:
        return move_box_v(box_pos, direction, boxes, obstacles)
    else:
        return move_box_h(box_pos, direction, boxes, obstacles)

def move_box_h(box_pos: complex, direction: complex, boxes: dict, obstacles: set):
    next_pos = box_pos + direction

    if next_pos in boxes:
        move_box_h(next_pos, direction, boxes, obstacles)
    boxes[next_pos] = boxes.pop(box_pos)

def move_box_v(box_pos: complex, direction: complex, boxes: dict, obstacles: set):
    b = boxes[box_pos]
    box_pos2 = box_pos + 1 if b == '[' else box_pos - 1
#    b2 = boxes[box_pos2]

    next_pos = box_pos + direction
    next_pos2 = box_pos2 + direction

    if next_pos in boxes:
        move_box(next_pos, direction, boxes, obstacles)
    boxes.pop(box_pos)
    boxes[next_pos] = b

    if next_pos2 in boxes:
        move_box(next_pos2, direction, boxes, obstacles)
    boxes[next_pos2] = boxes.pop(box_pos2)

def factor(boxes: dict[complex, str]) -> int:
    return sum(int(k.real + 100 * k.imag) for k,b in boxes.items() if b == '[')


matrix, directions = util.load_str_blocks('sample3.txt')
util.assert_equal(solve2(matrix, directions), 618, "Part 2, sample 3")

matrix, directions = util.load_str_blocks('sample2.txt')
util.assert_equal(solve2(matrix, directions), 9021, "Part 2, sample 2")

matrix, directions = util.load_str_blocks('input.txt')
util.assert_equal(solve2(matrix, directions), 1452348, "Part 2")
