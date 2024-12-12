import time
import util

def load_map(fname: str) -> tuple[set[complex], complex, complex, int, int]:
    obstacles = set()
    pos = 0j
    direction = 0j
    W = H = 0
    with open(util.full_name(fname), 'rt', encoding='utf-8') as f:
        for y,line in enumerate(f):
            H += 1
            W = len(line.rstrip())
            for x,c in enumerate(line.rstrip()):
                coord = x + y*1j
                if c == '#':
                    obstacles.add(coord)
                elif c in '^>v<':
                    pos = coord
                    if c == '^':
                        direction = -1j
                    elif c == '>':
                        direction = 1
                    elif c == 'v':
                        direction = 1j
                    elif c == '<':
                        direction = -1

    return obstacles, pos, direction, W, H

def solve1(obstacles, pos, direction, W, H) -> int:
    visited = set()
    while pos.real in range(W) and pos.imag in range(H):
        visited.add(pos)
        pos, direction = move(obstacles, pos, direction)

    return len(visited)

def move(obstacles, pos, direction) -> tuple[complex, complex]:
    if (pos + direction) in obstacles:
        return pos, direction * 1j # turn 90 degrees clockwise
    else:
        return pos + direction, direction

def solve2(obstacles, start_pos, start_direction, W, H) -> int:
    visited = set()
    pos, direction = start_pos, start_direction
    while pos.real in range(W) and pos.imag in range(H):
        visited.add(pos)
        pos, direction = move(obstacles, pos, direction)

    # Place obstacles only on visited positions to exclude useless checks.
    # It is 5 times faster
    count = 0
    for new_obs in visited:
        if new_obs not in [start_pos, start_pos + start_direction]:
            obstacles.add(new_obs)
            if is_cycled(obstacles, start_pos, start_direction, W, H):
                count += 1
                if count % 100 == 0:
                    print(f'{count}/{len(visited)}')
            obstacles.remove(new_obs)
    return count

def is_cycled(obstacles, pos, direction, W, H) -> bool:
    visited = set()
    while pos.real in range(W) and pos.imag in range(H):
        if (pos, direction) in visited:
            return True
        visited.add((pos,direction))
        #pos, direction = move(obstacles, pos, direction)
        if (pos + direction) in obstacles:
            direction *= 1j # turn 90 degrees clockwise
        else:
            pos += direction
    
    return False

obstacles, pos, direction, W, H = load_map('input_sample.txt')
util.assert_equal(solve1(obstacles, pos, direction, W, H), 41, "Part1 sample")
util.assert_equal(solve2(obstacles, pos, direction, W, H), 6, "Part2 sample")

obstacles, pos, direction, W, H = load_map('input.txt')
util.assert_equal(solve1(obstacles, pos, direction, W, H), 4819, "Part1")

start = time.time()
util.assert_equal(solve2(obstacles, pos, direction, W, H), 1796, "Part2")
period = time.time() - start
print(f'Part2. Time taken: {period:.2f} sec')