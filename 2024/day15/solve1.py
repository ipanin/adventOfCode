import util

def solve1(lines: list[str], direction_lines: list[str]) -> int:
    obstacles = set()
    boxes = set()
    robot = 1j
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            pos = x + y * 1j
            if c == '#':
                obstacles.add(pos)
            elif c == 'O':
                boxes.add(pos)
            elif c == '@':
                robot = pos

    for line in direction_lines:
        for d in line.rstrip():
            direction = util.DIRECTION_MAP[d]
            robot = move(robot, direction, boxes, obstacles)

    return factor(boxes)

def move(robot: complex, direction: complex, boxes: set, obstacles: set) -> complex:
    next_pos = robot + direction

    if next_pos in obstacles:
        return robot
    elif next_pos not in boxes:
        return next_pos
    elif try_move(next_pos, direction, boxes, obstacles):
        return next_pos
    else:
        return robot

def try_move(box_pos: complex, direction: complex, boxes: set, obstacles: set) -> bool:
    next_pos = box_pos + direction

    if next_pos in obstacles:
        return False
    elif next_pos not in boxes:
        boxes.add(next_pos)
        boxes.remove(box_pos)
        return True
    elif try_move(next_pos, direction, boxes, obstacles):
        boxes.add(next_pos)
        boxes.remove(box_pos)
        return True
    else:
        return False

def factor(boxes: set) -> int:
    return sum(int(b.real + 100 * b.imag) for b in boxes)


matrix, directions = util.load_str_blocks('sample1.txt')
util.assert_equal(solve1(matrix, directions), 2028, "Part 1, sample 1")

matrix, directions = util.load_str_blocks('input.txt')
util.assert_equal(solve1(matrix, directions), 1430536, "Part 1")
