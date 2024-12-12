lines = [(line[0], int(line[1:])) for line in open('day12/input.txt')]
DIRS = {'N': 1j, 'S': -1j, 'E': 1, 'W': -1}
part1 = part2 = 0j
dir = 1+0j
wp = 10+1j
for a, v in lines:
    if a in DIRS: 
        part1 += DIRS[a] * v
        wp    += DIRS[a] * v
    elif a == 'L': 
        dir *= 1j ** (v // 90)
        wp  *= 1j ** (v // 90)
    elif a == 'R': 
        dir *= (-1j) ** (v // 90)
        wp  *= (-1j) ** (v // 90)
    elif a == 'F':
        part1 += v * dir
        part2 += v * wp
    else:
        print('Unexpected action', a, v)
        
print("Part 1:", int(abs(part1.real)+abs(part1.imag)))
print("Part 2:", int(abs(part2.real)+abs(part2.imag)))
