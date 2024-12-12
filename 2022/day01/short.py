data = []
with open("input.txt", 'rt') as f:
    blocks = f.read().rstrip().split('\n\n')
    data = [sum(int(line) for line in b.split('\n')) for b in blocks]

print("Part 1.", max(data))
print("Part 2.", sum(sorted(data)[-3:]))

