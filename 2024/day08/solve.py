import util

def load_map(fname: str) -> tuple[dict[str, list[complex]], int, int]:
    antennas = dict()
    w = h = 0 # width and height
    with open(util.full_name(fname), 'rt', encoding='utf-8') as f:
        for y,line in enumerate(f):
            h += 1
            w = len(line.rstrip())
            for x,c in enumerate(line.rstrip()):
                coord = x + y*1j
                if c == '.':
                    continue
                else:
                    if c not in antennas:
                        antennas[c] = [coord]
                    antennas[c].append(coord) # check
    return antennas, w, h

def solve1(antennas, W, H) -> int:
    antinodes = set()
    for ant_list in antennas.values():
        for ant1 in ant_list:
            for ant2 in ant_list:
                if ant1 != ant2:
                    mark_antinodes(ant1, ant2, W, H, antinodes)
    return len(antinodes)

def mark_antinodes(ant1, ant2, W, H, antinodes):
    r = ant1 - ant2
    antinode1 = ant1 + r
    antinode2 = ant2 - r
    if antinode1.real in range(W) and antinode1.imag in range(H):
        antinodes.add(antinode1)
    if antinode2.real in range(W) and antinode2.imag in range(H):
        antinodes.add(antinode2)

def solve2(antennas, W, H) -> int:
    antinodes = set()
    for ant_list in antennas.values():
        for ant1 in ant_list:
            for ant2 in ant_list:
                if ant1 != ant2:
                    mark_antinodes2(ant1, ant2, W, H, antinodes)
    return len(antinodes)

def mark_antinodes2(ant1, ant2, W, H, antinodes):
    r = ant1 - ant2
    antinode = ant1 + r
    while antinode.real in range(W) and antinode.imag in range(H):
        antinodes.add(antinode)
        antinode += r

    antinode = ant2 - r
    while antinode.real in range(W) and antinode.imag in range(H):
        antinodes.add(antinode)
        antinode -= r

    antinodes.add(ant1)
    antinodes.add(ant2)

antennas, W, H = load_map('input_sample.txt')
util.assert_equal(solve1(antennas, W, H), 14, "Part1 sample")
util.assert_equal(solve2(antennas, W, H), 34, "Part2 sample")

antennas, W, H = load_map('input.txt')
util.assert_equal(solve1(antennas, W, H), 311, "Part1")
util.assert_equal(solve2(antennas, W, H), 1115, "Part2")