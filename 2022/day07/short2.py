# Solution from https://www.reddit.com/r/adventofcode/comments/zesk40/comment/iz8zntk/
# Не запоминаем имена директорий и файлов, сохраняем только суммарный размер.
# Работает при условии, что директория не будет посещаться дважды
stack = []
sizes = []

def up():
    sizes.append(stack.pop(-1))
    if stack:
        stack[-1] += sizes[-1]

for line in open("input.txt").readlines():
    match line.strip().split():
        case "$", "cd", "..": up()
        case "$", "cd", _: stack.append(0)
        case "$", _: pass # $ ls
        case "dir", _: pass
        case size, _: stack[-1] += int(size)

while stack:
    up()

print("Part1", sum(s for s in sizes if s <= 100000))
print("Part2", min(s for s in sizes if s >= (max(sizes) - 40000000)))