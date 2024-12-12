# https://www.reddit.com/r/adventofcode/comments/rca6vp/comment/hntjz0i/?utm_source=share&utm_medium=web2x&context=3
heights = [[int(c) for c in line.strip()] for line in open("input.txt").readlines()]
N = len(heights)
M = len(heights[0])

def neighbours(y, x):
    neighs = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
    return [(a, b) for a, b in neighs if 0 <= a < N and 0 <= b < M]


# Part 1
lowpoints = []
for y in range(N):
    for x in range(M):
        if all(heights[y][x] < heights[a][b] for a, b in neighbours(y, x)):
            lowpoints.append((y, x))

print("Part 1:", sum(heights[y][x] + 1 for y, x in lowpoints))


# Part 2
def get_basin(y, x):
    basin = {(y, x)}
    for a, b in neighbours(y, x):
        if heights[y][x] < heights[a][b] < 9:
            basin |= get_basin(a, b)
    return basin

a, b, c = sorted([len(get_basin(y, x)) for y, x in lowpoints])[-3:]
print("Part 2:", a*b*c)
